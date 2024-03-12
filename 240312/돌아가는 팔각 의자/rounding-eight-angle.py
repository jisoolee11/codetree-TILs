from collections import deque

def right_check(n, d):
    for i in range(n, 3):
        if table[i][2] == table[i+1][6]:
            rotate_num[i+1] = 0
            d = 0
        else:
            rotate_num[i+1] = -d
            d = -d


def left_check(n, d):
    for i in range(n, 0, -1):
        if table[i][6] == table[i-1][2]:
            rotate_num[i-1] = 0
            d = 0
        else:
            rotate_num[i-1] = -d
            d = -d


table = [deque(map(int, input())) for _ in range(4)]
k = int(input())

for _ in range(k):
    rotate_num = [2, 2, 2, 2]
    n, d = map(int, input().split())
    rotate_num[n-1] = d
    right_check(n-1, d)
    left_check(n-1, d)
    
    for i, t in enumerate(table):
        if rotate_num[i] == 1:
            t.rotate(1)
        elif rotate_num[i] == -1:
            t.rotate(-1)
        else:
            continue

result = 0
for i, t in enumerate(table):
    if i == 0:
        result += 1 * t[0]
    elif i == 1:
        result += 2 * t[0]
    elif i == 2:
        result += 4 * t[0]
    else:
        result += 8 * t[0]

print(result)