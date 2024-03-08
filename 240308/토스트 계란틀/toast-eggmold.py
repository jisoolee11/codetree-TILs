from collections import deque

def calc(e_list):
    total = 0
    for x, y in e_list:
        total += eggs[x][y]
    result = int(total/len(e_list))

    for x, y in e_list:
        eggs[x][y] = result


def bfs(start_x, start_y):
    dq = deque()
    test = []
    dq.append((start_x, start_y))
    visited[start_x][start_y] = 1
    test.append((start_x, start_y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if L <= abs(eggs[x][y] - eggs[nx][ny]) <= R:
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
                    test.append((nx, ny))

    return test


n, L, R = map(int, input().split())
eggs = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

cnt = 0
while True:
    is_move = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                e_list = bfs(i, j)
                if len(e_list) > 1:
                    is_move = True
                calc(e_list)

    if is_move:
        cnt += 1

    break

print(cnt)