from collections import deque

FACE_NUM = 6
OUT_OF_GRID = (-1, -1)

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 현재 위치와 방향을 기록합니다. (시작은 오른쪽)
x, y = 0, 0
move_dir = 0

# 방향은 오른쪽, 아래, 왼쪽, 위 순입니다.
# 시계방향, 반시계방향 회전을 용이하게 하기 위한 순서로 정의합니다.
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 주사위가 놓여있는 상태 
up, front, right = 1, 2, 3

# bfs 진행을 위해 필요한 값들입니다.
bfs_q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0


# 격자 안에 있는지를 확인합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 동일한 숫자에 대해서만 이동이 가능합니다.
def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == target_num


def bfs(x, y, target_num):
    # visited 값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 시작점을 표시합니다.
    visited[x][y] = True
    bfs_q.append((x, y))

    score = 0

    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        score += target_num

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            if can_go(new_x, new_y, target_num):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True

    return score


# 현재 위치를 기준으로 했을 때의 점수를 계산합니다.
def get_score():
    return bfs(x, y, grid[x][y])


# 해당 방향으로 이동했을 때의 다음 위치를 구합니다.
# 이동이 불가능할 경우 OUT_OF_GRID를 반환합니다.
def next_pos():
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    return (nx, ny) if in_range(nx, ny) else OUT_OF_GRID


def simulate():
    global ans
    global x, y, move_dir
    global up, front, right
    
    # 현재 방향으로 굴렸을 때의 격자상의 위치를 구합니다.
    nx, ny = next_pos()

    # 격자를 벗어난다면, 방향을 반대로 튼 이후의 격자를 구합니다.
    if (nx, ny) == OUT_OF_GRID:
        move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        nx, ny = next_pos()
    
    # 위치를 이동합니다.
    x, y = nx, ny

    # 점수를 더해줍니다.
    ans += get_score()
    
    # 주사위가 놓여있는 상태를 조정합니다.
    if move_dir == 0: # 오른쪽
        up, front, right = 7 - right, front, up
    elif move_dir == 1: # 아래쪽
        up, front, right = 7 - front, up, right
    elif move_dir == 2: # 왼쪽
        up, front, right = right, front, 7 - up
    else: # 위쪽
        up, front, right = front, 7 - up, right
    
    # 주사위의 바닥면에 적혀있는 숫자와, 격자 숫자를 비교합니다.
    bottom = 7 - up
    # 주사위에 적힌 숫자가 더 크면 시계방향으로 90' 회전합니다.
    if bottom > grid[x][y]:
        move_dir = (move_dir + 1) % 4
    # 주사위에 적힌 숫자가 더 작으면 반시계방향으로 90' 회전합니다.
    elif bottom < grid[x][y]:
        move_dir = (move_dir - 1 + 4) % 4


# 시뮬레이션 진행
for _ in range(m):
    simulate()

# 점수 출력
print(ans)