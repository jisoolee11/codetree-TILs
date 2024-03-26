# 변수 선언 및 입력
n, L = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr = [0 for _ in range(n)]

# 각 칸마다 경사로가 몇 번씩
# 놓여졌는지를 해당 배열에 적어줍니다.
# 경사로가 겹쳐 놓여지는지를
# 확인하기 위해 필요합니다.
ramp_cnt = [0 for _ in range(n)]


# arr의 [l, r] 구간에 있는 원소가 
# 전부 동일한 원소인지 확인합니다.
def all_same(l, r):
    return len(set(arr[l:r + 1])) == 1


# 해당 arr가 지나갈 수 있는 경우인지 확인합니다.
def can_pass():
    global ramp_cnt
    
    #Step 1.
    #먼저 인접한 곳의 높이 차가 2 이상인 곳이 있는지 
    #확인합니다. 존재한다면, 불가능합니다.
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) >= 2:
            return False
    
    #각 위치마다 경사로의 개수를 0으로 초기화합니다.
    ramp_cnt = [0 for _ in range(n)]
    
    # Step2. 꼭 놓아야 할 경사로를 확인합니다.
    
    # Step2-1. ◣ 직각삼각형이 필요한 곳을 찾습니다.
    for i in range(n - 1):
        # [i + 1, i + L] 까지 경사로를 놓아야만 하는 경우입니다.
        if arr[i] == arr[i + 1] + 1:
            # L만큼의 여유 공간이 있는지 확인합니다.
            # 없다면 불가능합니다.
            if i + L >= n:
                return False
            
            # 경사로가 놓일 곳의 높이가 전부 같은지 확인합니다.
            # 전부 같지 않다면 불가능합니다.
            if not all_same(i + 1, i + L):
                return False
            
            # 경사로가 놓이는 곳에 개수를 갱신합니다.
            for j in range(i + 1, i + L + 1):
                ramp_cnt[j] += 1
				
	# Step2-2. ◢ 직각삼각형이 필요한 곳을 찾습니다.
    for i in range(1, n):
        # [i - L, i - 1] 까지 경사로를 놓아야만 하는 경우입니다.
        if arr[i] == arr[i - 1] + 1:
            # L만큼의 여유 공간이 있는지 확인합니다.
            # 없다면 불가능합니다.
            if i - L < 0:
                return False
            
            # 경사로가 놓일 곳의 높이가 전부 같은지 확인합니다.
            # 전부 같지 않다면 불가능합니다.
            if not all_same(i - L, i - 1):
                return False
            
            # 경사로가 놓이는 곳에 개수를 갱신합니다.
            for j in range(i - L, i):
                ramp_cnt[j] += 1
    
    # Step3.
    # 꼭 놓아야 했던 경사로끼리
    # 겹쳐 놓였는지 확인합니다.
    # 그랬다면, 불가능합니다.
    if any([cnt >= 2 for cnt in ramp_cnt]):
        return False
    
    # 모든 조건을 만족했다면, 가능한 경우입니다.
    return True


ans = 0
    
# row번째 행이 지나갈 수 있는 곳인지 확인합니다.
for row in range(n):
    # 확인하고 싶은 수열을 입력합니다.
    for col in range(n):
        arr[col] = grid[row][col]

    # 지나갈 수 있다면 답을 갱신합니다.
    if can_pass():
        ans += 1

# column번째 열이 지나갈 수 있는 곳인지 확인합니다.
for col in range(n):
    # 확인하고 싶은 수열을 입력합니다.
    for row in range(n):
        arr[row] = grid[row][col]

    # 지나갈 수 있다면 답을 갱신합니다.
    if can_pass():
        ans += 1

print(ans)