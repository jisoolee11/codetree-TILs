from collections import deque
import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
hospitals = []
selected_hos = []

dq = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[False for _ in range(n)] for _ in range(n)]

ans = INT_MAX

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    

def can_go(x, y):
    return in_range(x, y) and a[x][y] != 1 and not visited[x][y]


def push(x, y, new_step):
    dq.append((x, y))
    visited[x][y] = True
    step[x][y] = new_step


def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = step[i][j] = 0


def find_max_dist():
    while dq:
        x, y = dq.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                push(new_x, new_y, step[x][y]+1)

    max_dist = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                if visited[i][j]:
                    max_dist = max(max_dist, step[i][j])
                else:
                    max_dist = INT_MAX

    return max_dist


def elapsed_time_to_kill_all_virus():
    initialize()
    
    for i in range(len(selected_hos)):
        x, y = selected_hos[i]
        push(x, y, 0)

    max_elapsed_time = find_max_dist()
    return max_elapsed_time


def find_min_time(curr_idx, cnt):
    global ans

    if cnt == m:
        ans = min(ans, elapsed_time_to_kill_all_virus())
        return

    if curr_idx == len(hospitals):
        return

    find_min_time(curr_idx+1, cnt)

    selected_hos.append(hospitals[curr_idx])
    find_min_time(curr_idx+1, cnt+1)
    selected_hos.pop()


for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            hospitals.append((i, j))

find_min_time(0, 0)
if ans == INT_MAX:
    ans = -1

print(ans)