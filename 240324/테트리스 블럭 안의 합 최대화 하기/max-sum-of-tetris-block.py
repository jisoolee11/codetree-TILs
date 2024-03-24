def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    return in_range(x, y) and (x, y) not in visited


def get_max_sum(cnt, sum_of_nums):
    global max_sum

    if cnt == 4:
        max_sum = max(max_sum, sum_of_nums)
        return

    for x, y in visited:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if can_go(nx, ny):
                visited.append((nx, ny))
                get_max_sum(cnt+1, sum_of_nums+board[nx][ny])
                visited.pop()

    return


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = []
max_sum = 0

for i in range(n):
    for j in range(m):
        visited.append((i, j))
        get_max_sum(1, board[i][j])
        visited.pop()

print(max_sum)