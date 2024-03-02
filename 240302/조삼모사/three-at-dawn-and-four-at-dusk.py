def calc():
    morning_work = 0
    evening_work = 0
    for i in range(n):
        for j in range(n):
            if i in morning_works_idx and j in morning_works_idx:
                morning_work += works[i][j]
            elif i not in morning_works_idx and j not in morning_works_idx:
                evening_work += works[i][j]

    return abs(morning_work - evening_work)


def dfs(i):
    global result

    if len(morning_works_idx) == n // 2:
        result = min(calc(), result)
        return
    
    for i in range(i, n):
        if not visited[i]:
            visited[i] = True
            morning_works_idx.append(i)
            dfs(i+1)
            visited[i] = False
            morning_works_idx.pop()


n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
morning_works_idx = []
result = 100

dfs(0)
print(result)