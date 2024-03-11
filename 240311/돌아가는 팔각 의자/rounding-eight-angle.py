from collections import deque

def right_check(idx):
    if table[idx][2] == table[idx+1][6]:
        return True
    else:
        return False


def left_check(idx):
    if table[idx][6] == table[idx-1][2]:
        return True
    else:
        return False


def rotate_dir():
    for i in range(4):
        if t_rotate[i] != 0:
            if i == 0:
                if t_rotate[i+1] == 0:
                    if not right_check(i):
                        t_rotate[i+1] = -t_rotate[i]
                    else: 
                        t_rotate[i+1] = 2
            elif i == 3:
                if t_rotate[i-1] == 0:
                    if not left_check(i):
                        t_rotate[i-1] = -t_rotate[i]
                    else: 
                        t_rotate[i-1] = 2
            else:
                if t_rotate[i+1] == 0:
                    if not right_check(i):
                        t_rotate[i+1] = -t_rotate[i]
                    else:
                        t_rotate[i+1] = 2
                if t_rotate[i-1] == 0:
                    if not left_check(i):
                        t_rotate[i-1] = -t_rotate[i]
                    else:
                        t_rotate[i-1] = 2


def calc():
    global result

    for idx, t in enumerate(table):
        if t[0] == 1:
            if idx == 0:
                result += 1
            elif idx == 1:
                result += 2
            elif idx == 2:
                result += 4
            else:
                result += 8


table = [deque(map(int, input())) for _ in range(4)]
k = int(input())
result = 0
for _ in range(k):
    n, d = map(int, input().split())
    t_rotate = [0, 0, 0, 0]
    t_rotate[n-1] = d
    rotate_dir()
    for idx, t in enumerate(table):
        if t_rotate[idx] == 2:
            continue
        else:
            t.rotate(t_rotate[idx])

calc()

print(result)