def tree_growth():
    growth = []
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                        cnt += 1
                growth.append((x, y, cnt))

    for x, y, c in growth:
        board[x][y] += c

    return growth


def tree_propagation(growth):
    propagation = []
    for x, y, _ in growth:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and herbicide[nx][ny] == 0:
                cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and herbicide[nx][ny] == 0:
                propagation.append((nx, ny, int(board[x][y]/cnt)))

    for x, y, p in propagation:
        board[x][y] += p


def tree_herbicide():
    herbicide_cnt = []
    for x in range(n):
        for y in range(n):
            cnt = 0
            if board[x][y] >= 0:
                cnt += board[x][y]
                for i in range(4, 8):
                    for j in range(1, k+1):
                        nx = x + (dx[i])*j
                        ny = y + (dy[i])*j
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] >= 0:
                                cnt += board[nx][ny]
                            else:
                                break
            herbicide_cnt.append((x, y, cnt))

    herbicide_cnt.sort(key = lambda x: (-x[2], x[0], x[1]))

    return herbicide_cnt[0]


n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0, -1, 1, 1, -1], [0, 1, 0, -1, 1, 1, -1, -1]
herbicide = [[0] * n for _ in range(n)]
result = 0

for _ in range(m):
    growth = tree_growth()
    tree_propagation(growth)
    max_herbicide = tree_herbicide()
    result += max_herbicide[2]

    herbicide[max_herbicide[0]][max_herbicide[1]] = c + 1
    for i in range(4, 8):
        for j in range(1, k+1):
            nx = max_herbicide[0] + (dx[i])*j
            ny = max_herbicide[1] + (dy[i])*j
            if 0 <= nx < n and 0 <= ny < n:
                herbicide[nx][ny] = c + 1
                if board[nx][ny] == -1 or board[nx][ny] == 0:
                    break

    for i in range(n):
        for j in range(n):
            if herbicide[i][j] > 0:
                herbicide[i][j] -= 1
                board[i][j] = 0

print(result)