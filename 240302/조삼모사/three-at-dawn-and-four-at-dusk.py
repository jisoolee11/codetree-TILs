import sys

INT_MAX = sys.maxsize


def calc():
    morning_work = 0
    evening_work = 0
    for i in range(n):
        for j in range(n):
            if not evening[i] and not evening[j]:
                morning_work += works[i][j]
            elif evening[i] and evening[j]:
                evening_work += works[i][j]

    return abs(morning_work - evening_work)


def dfs(i, cnt):
    global result

    if cnt == n // 2:
        result = min(calc(), result)
        return

    if i == n:
        return
    
    dfs(i+1, cnt)

    evening[i] = True
    dfs(i+1, cnt+1)
    evening[i] = False



n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
evening = [False] * n

result = INT_MAX

dfs(0, 0)
print(result)