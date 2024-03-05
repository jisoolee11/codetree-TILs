def n_move():
    global nutrients

    n_new_move = []
    for x, y in nutrients:
        nx = (x + dx[d-1]*p) % n
        ny = (y + dy[d-1]*p) % n
        n_new_move.append((nx, ny))

    nutrients = n_new_move


def grow():
    global nutrients

    for x, y in nutrients:
        board[x][y] += 1

    grow_board = [[0] * n for _ in range(n)]
    for x, y in nutrients:
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                grow_board[x][y] += 1

    for i in range(n):
        for j in range(n):
            if grow_board[i][j]:
                board[i][j] += grow_board[i][j]


def cut_down():
    global nutrients

    cut_down_tree = []
    for i in range(n):
        for j in range(n):
            if (i, j) in nutrients:
                continue
            else:
                if board[i][j] >= 2:
                    board[i][j] -= 2
                    cut_down_tree.append((i, j))

    nutrients = cut_down_tree


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]
nutrients = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)]

for _ in range(m):
    d, p = map(int, input().split())
    n_move()
    grow()
    cut_down()

result = 0
for i in range(n):
    result += sum(board[i])

print(result)