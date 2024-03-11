def forward(x, y, dd):
    global start_x, start_y, d

    d = (dd-1) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and board[nx][ny] != 1:
        start_x, start_y = nx, ny
        visited[nx][ny] = 1
        return True
    elif visited[nx][ny] == 1 or board[nx][ny] == 1:
        dir_check[d] = False
        return False


n, m = map(int, input().split())
start_x, start_y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dir_check = [True] * 4

visited[start_x][start_y] = 1

while True:
    if forward(start_x, start_y, d):
        dir_check = [True] * 4
        continue

    if True not in dir_check:
        nx = start_x + dx[(d-2)%4]
        ny = start_y + dy[(d-2)%4]
        if board[nx][ny] == 0:
            start_x, start_y = nx, ny
            dir_check = [True] * 4
        else:
            break

result = 0
for v in visited:
    result += sum(v)

print(result)