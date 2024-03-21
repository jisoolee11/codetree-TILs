def curve(start, g):
    if g == 0:
        return
    for i in range(len(start)-1, 0, -1):
        ex, ey = start[-1][0], start[-1][1]
        d = start[i][2]
        start.append((ex + dx[d], ey + dy[d], (d+1)%4))
    
    curve(start, g-1)

    for x, y, d in start:
        dragon_curve.append((x, y))
    

n = int(input())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
dragon_curve = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    start = []
    start.append((x, y, d))
    start.append((x + dx[d], y + dy[d], (d+1)%4))
    curve(start, g)

dragon_curve = list(set(dragon_curve))

max_x = max(dragon_curve, key=lambda x: x[0])[0] + 1
max_y = max(dragon_curve, key=lambda x: x[1])[1] + 1

board = [[0] * max_y for _ in range(max_x)]

for x, y in dragon_curve:
    if board[x][y] == 0:
        board[x][y] = 1

cnt = 0
for i in range(max_x-1):
    for j in range(max_y-1):
        if board[i][j] == 1:
            if board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
                cnt += 1

print(cnt)