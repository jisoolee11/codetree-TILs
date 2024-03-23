from collections import deque

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

empty_places = list()
selected_indices = list()
bfs_q = deque()
max_empty_cnt = 0

# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(x, y):
    return 0 <= x and x < n and 0 <= y and y < m and \
                  not visited[x][y] and grid[x][y] != 1


# visited 배열을 초기화해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


# 선택된 위치에 방화벽을 설치합니다.
def place_firewalls():
    for i in range(len(selected_indices)):
        idx = selected_indices[i]
        curr_x, curr_y = empty_places[idx]
        
        grid[curr_x][curr_y] = 1
        
        
# 다음 탐색을 위해 설치했던 방화벽을 제거합니다.
def remove_firewalls():
    for i in range(len(selected_indices)):
        idx = selected_indices[i]
        curr_x, curr_y = empty_places[idx]
        
        grid[curr_x][curr_y] = 0
        
        
def bfs():
    # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
        
            if can_go(new_x, new_y):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True

# 선택된 빈 칸에 방화벽을 설치했을 때 영역의 크기를 구합니다.
def get_area():
    global max_empty_cnt 
    
    # BFS 탐색을 위한 초기화 작업을 수행합니다.
    initialize_visited()
    place_firewalls()
    
    # 격자를 순회하며 불이 존재하는 경우
    # BFS 탐색을 통해 해당 불이 방문하게 되는 영역을 구합니다.
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 2:
                bfs_q.append((i, j))
                visited[i][j] = True
                bfs()
                
    # BFS 탐색 과정에서 방문한 적이 없는 빈 칸의 개수를 세줍니다.
    empty_cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 0:
                empty_cnt += 1
    
    max_empty_cnt = max(empty_cnt, max_empty_cnt)
    
    # 탐색이 끝난 뒤 설치한 방화벽을 제거해줍니다.
    remove_firewalls()
    
    
def search_combinations(curr_idx, cnt):
    if cnt == 3:
        get_area()
        return
    
    if curr_idx == len(empty_places):
        return
    
    selected_indices.append(curr_idx)
    search_combinations(curr_idx + 1, cnt + 1)
    selected_indices.pop()
    
    search_combinations(curr_idx + 1, cnt)
    

# 빈 칸인 경우 가능한 조합을 탐색하기 위해
# 배열에 따로 저장해줍니다.
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            empty_places.append((i, j))
            
search_combinations(0, 0)
print(max_empty_cnt)