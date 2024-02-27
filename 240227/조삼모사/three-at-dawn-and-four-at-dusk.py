n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]
evening = [False] * n
result = 100


def calulate():
    sum_morning = sum([
        P[i][j] 
        for i in range(n) 
        for j in range(n) 
        if not evening[i] and not evening[j]
    ])
    sum_evening = sum([
        P[i][j] 
        for i in range(n) 
        for j in range(n) 
        if evening[i] and evening[j]
    ])

    return abs(sum_morning - sum_evening)


def find_min(cur_idx, cnt):
    global result

    if cnt == n // 2:
        result = min(result, calulate())
        return

    if cur_idx == n:
        return

    find_min(cur_idx+1, cnt)

    evening[cur_idx] = True
    find_min(cur_idx+1, cnt+1)
    evening[cur_idx] = False


find_min(0, 0)

print(result)