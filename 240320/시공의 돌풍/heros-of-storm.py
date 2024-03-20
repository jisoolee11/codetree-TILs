def diffusion():
    new_dust = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if dust[x][y] != -1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and dust[nx][ny] != -1:
                        new_dust[nx][ny] += int(dust[x][y]/5)
                        cnt += 1
                dust[x][y] -= int(dust[x][y]/5) * cnt 

    for x in range(n):
        for y in range(m):
            if dust[x][y] != -1:
                dust[x][y] += new_dust[x][y]


def find_storm():
    for x in range(n):
        for y in range(m):
            if dust[x][y] == -1:
                storm = (x, y)
                return storm


def clean_up(x, y):
    ux, uy = [0, -1, 0, 1], [1, 0, -1, 0]
    curr_dust = dust[x][y]
    for i in range(4):
        while True:
            nx = x + ux[i]
            ny = y + uy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or dust[nx][ny] == -1:
                break
            else:
                if dust[x][y]== -1:
                     curr_dust = 0
                next_dust = dust[nx][ny]
                dust[nx][ny] = curr_dust
                x, y = nx, ny
                curr_dust = next_dust


def clean_down(x, y):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    curr_dust = dust[x][y]
    for i in range(4):
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or dust[nx][ny] == -1:
                break
            else:
                if dust[x][y]== -1:
                     curr_dust = 0
                next_dust = dust[nx][ny]
                dust[nx][ny] = curr_dust
                x, y = nx, ny
                curr_dust = next_dust
    

n, m, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(t):
    diffusion()
    sx, sy = find_storm()
    clean_up(sx, sy)
    clean_down(sx+1, sy)

result = 0
for i in range(n):
    result += sum(dust[i])

print(result+2)