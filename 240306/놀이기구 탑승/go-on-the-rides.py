def like_friends(n0, num):
    friend = []
    for x in range(n):
        for y in range(n):
            f, b = 0, 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in num:
                        f += 1
                    elif not board[nx][ny]:
                        b += 1

            friend.append((f, b, x, y))

    friend = sorted(friend, key=lambda x: (-x[0], -x[1], x[2], x[3]))

    for f, b, x, y in friend:
        if board[x][y]:
            continue
        else:
            return (f, b, x, y)


def calc():
    global result

    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in students_num[board[x][y]]:
                        cnt += 1

            if cnt == 1:
                result += 1
            elif cnt == 2:
                result += 10
            elif cnt == 3:
                result += 100
            elif cnt == 4:
                result += 1000

                    
n = int(input())
board = [[0] * n for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
students_num = [[] for _ in range(n*n+1)]
result = 0

for _ in range(n*n):
    n0, *num = map(int, input().split())
    students_num[n0].extend(num)
    student = like_friends(n0, num)
    board[student[2]][student[3]] = n0

calc()

print(result)