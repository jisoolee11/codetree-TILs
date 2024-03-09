import sys

INF_MAX = sys.maxsize

def calc():
    total = 0
    for px, py in person:
        min_h = INF_MAX
        for hx, hy in selected_h:
            dist = abs(hx-px) + abs(hy-py)
            min_h = min(min_h, dist)
        total += min_h
    
    return total

def backtracking(cnt, idx):
    global result

    if cnt == m:
        result = min(result, calc())
        return

    for i in range(idx, len(hospitals)):
        if not visited[i]:
            visited[i] = True
            selected_h.append(hospitals[i])
            backtracking(cnt+1, i+1)
            visited[i] = False
            selected_h.pop()


n, m = map(int, input().split())
person, hospitals = [], []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            person.append((i, j))
        elif row[j] == 2:
            hospitals.append((i, j))

visited = [False] * len(hospitals)
selected_h = []
result = INF_MAX

backtracking(0, 0)

print(result)