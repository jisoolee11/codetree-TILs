def dice_move(dice, d):
    if d == 1:
        new_dice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    elif d == 2:
        new_dice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    elif d == 3:
        new_dice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
    elif d == 4:
        new_dice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]

    return new_dice
        

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
# 위, 앞, 오, 뒤, 왼, 아
dice = [0, 0, 0, 0, 0, 0]
if board[x][y] != 0:
    dice[-1] = board[x][y]

for d in direction:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        dice = dice_move(dice, d)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])
    else:
        continue