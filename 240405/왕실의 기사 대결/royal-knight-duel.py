from collections import deque

def bfs(i, d):
    global knights_hp, knights_board, knights

    new_board = [[0] * L for _ in range(L)]
    visited = [0] * (N+1)
    dq = deque()
    for ox, oy, idx in knights[i]:
        dq.append((ox, oy, idx))
        visited[idx] = 1

    while dq:
        x, y, idx = dq.popleft()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < L and 0 <= ny < L and board[nx][ny] != 2:
            new_board[nx][ny] = idx
            if knights_board[nx][ny] and knights_board[nx][ny] != idx:
                for ox, oy, idx in knights[knights_board[nx][ny]]:
                    dq.append((ox, oy, idx))
                    visited[idx] = 1
        else:
            return False

    for mx in range(L):
        for my in range(L):
            if new_board[mx][my] and new_board[mx][my] != i and board[mx][my] == 1:
                knights_hp[new_board[mx][my]] -= 1

    remove = []
    for idx, d in enumerate(knights_hp):
        if d > 0:
            continue
        else:
            remove.append(idx)

    for x in range(L):
        for y in range(L):
            if new_board[x][y] in remove:
                new_board[x][y] = 0

    knights = [[] for _ in range(N+1)]
    for x in range(L):
        for y in range(L):
            knights[new_board[x][y]].append((x, y, new_board[x][y]))

    for v in range(1, N+1):
        if visited[v] == 0:
            for x in range(L):
                for y in range(L):
                    if knights_board[x][y] == v:
                        new_board[x][y] = v

    knights_board = new_board
            
    return True


L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
knights_board = [[0] * L for _ in range(L)]
knights = [[] for _ in range(N+1)]
knights_hp = [0]
knights_ohp = [0]
knights_area = [()]
for idx in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    knights_hp.append(k)
    knights_ohp.append(k)
    knights_area.append((h, w))
    for i in range(r-1, r+h-1):
        for j in range(c-1, c+w-1):
            knights_board[i][j] = idx
            knights[idx].append((i, j, idx))

for _ in range(Q):
    i, d = map(int, input().split())
    bfs(i, d)

result = 0
for o, h in zip(knights_ohp, knights_hp):
    if h == 0:
        continue
    else:
        result += o - h

print(result)