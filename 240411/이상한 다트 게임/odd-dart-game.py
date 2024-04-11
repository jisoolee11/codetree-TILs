BLANK = 0
CW = 0
CCW = 1

# 변수 선언 및 입력:
n, m, q = tuple(map(int, input().split()))
plate = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [BLANK for _ in range(m)]
removed = [
    [False for _ in range(m)]
    for _ in range(n)
]


def shift(row, d, k):
    # Step1. temp 배열을 초기화합니다.
    for col in range(m):
        temp[col] = BLANK
    
    # Step2. 회전을 진행합니다.
    # 시계방향 회전시에는, 
    # 1차원 배열을 오른쪽으로 k칸 밀어준다고
    # 생각할 수 있습니다.
    if d == CW:
        for col in range(m):
            temp[(col + k) % m] = plate[row][col]
    else:
        for col in range(m):
            temp[(col - k + m) % m] = plate[row][col]
    
    # Step3. 회전 이후의 결과인 temp 값을
    # 다시 plate에 옮겨줍니다.
    for col in range(m):
        plate[row][col] = temp[col]


def rotate(x, d, k):
    # x 배수에 대해서만 밀어주는 작업을 진행합니다.
    for i in range(n):
        if (i + 1) % x == 0:
            shift(i, d, k)
            

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def remove():
    is_removed = False
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # Step1. removed 배열을 초기화합니다.
    for x in range(n):
        for y in range(m):
            removed[x][y] = False
    
    # Step2. 인접한 숫자 중 같은 쌍을 찾아
    # 지워야 한다는 표시를 합니다.
    # 이때, 열에 대해서는 원형으로 이루어진 판이기 때문에
    # 양쪽 경계에서 인접한 곳의 위치를 구하는 부분에 유의합니다.
    for x in range(n):
        for y in range(m):
            if plate[x][y] == BLANK:
                continue
            
            for dx, dy in zip(dxs, dys):
                # 열에 대해서는 원형으로 이어져있습니다.
                nx, ny = x + dx, (y + dy + m) % m
                if in_range(nx, ny) and plate[nx][ny] == plate[x][y]:
                    removed[x][y] = removed[nx][ny] = True
    
    # Step3. 지워야 할 부분들을 전부 지워줍니다.
    for x in range(n):
        for y in range(m):
            if removed[x][y]:
                is_removed = True
                plate[x][y] = BLANK
    
    return is_removed


def normalize():
    total_sum, cnt = 0, 0
    for i in range(n):
        for j in range(m):
            if plate[i][j] != BLANK:
                total_sum += plate[i][j];
                cnt += 1
    
    # 남아 있는 숫자가 있을 경우에만 정규화를 진행합니다.
    if cnt > 0:
        avg = total_sum // cnt
        
        for i in range(n):
            for j in range(m):
                if plate[i][j] == BLANK:
                    continue
                
                if plate[i][j] < avg:
                    plate[i][j] += 1
                elif plate[i][j] > avg:
                    plate[i][j] -= 1
                

def simulate(x, d, k):
    # Step1. 회전을 진행합니다.
    rotate(x, d, k)
    
    # Step2. 인접하며 동일한 숫자를 찾아 지웁니다.
    is_removed = remove()
    
    # Step3. 지워진 숫자가 없다면, 정규화를 진행합니다.
    if not is_removed:
        normalize()

        
# q번에 걸쳐 시뮬레이션을 진행합니다.
for _ in range(q):
    x, d, k = tuple(map(int, input().split()))
    simulate(x, d, k)

ans = sum([
    plate[i][j]
    for i in range(n)
    for j in range(m)
    if plate[i][j] != BLANK
])

print(ans)