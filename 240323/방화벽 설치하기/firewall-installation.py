from collections import deque

def cnt_blank(new_board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0 and board[i][j] == 0:
                cnt += 1

    return cnt


def create_fire(fx, fy, new_board):
    dq = deque()
    dq.append((fx, fy))
    new_board[fx][fy] = 1

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not new_board[nx][ny] and not board[nx][ny]:
                    dq.append((nx, ny))
                    new_board[nx][ny] = 1

    return new_board


def create_board(wall):
    n_board = [[0] * m for _ in range(n)]

    for x, y in wall:
        n_board[x][y] = 1
    
    return n_board


def create_wall(cnt, x, y):
    global result

    if cnt == 3:
        new_board = create_board(wall)
        for fx, fy in fire:
            new_board = create_fire(fx, fy, new_board) 

        result = max(result, cnt_blank(new_board))
        return

    for i in range(x, n):
        for j in range(y, m):
            if visited[i][j] == 0 and board[i][j] == 0:
                wall.append((i, j))
                visited[i][j] = 1
                if j == m-1:
                    create_wall(cnt+1, i+1, 0)
                else:
                    create_wall(cnt+1, i, j+1)
                wall.pop()
                visited[i][j] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
wall = []
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
fire = []
result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            fire.append((i, j))

create_wall(0, 0, 0)

print(result)