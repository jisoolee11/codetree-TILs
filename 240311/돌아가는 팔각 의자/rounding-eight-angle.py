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
    rotate = [0, 0, 0, 0]
    rotate[n-1] = d
    while 0 in rotate:
        for i in range(4):
            if rotate[i] != 0:
                if i == 0:
                    if rotate[i+1] == 0:
                        if not right_check(i):
                            rotate[i+1] = -rotate[i]
                        else: 
                            rotate[i+1] = 2
                elif i == 3:
                    if rotate[i-1] == 0:
                        if not left_check(i):
                            rotate[i-1] = -rotate[i]
                        else: 
                            rotate[i-1] = 2
                else:
                    if rotate[i+1] == 0:
                        if not right_check(i):
                            rotate[i+1] = -rotate[i]
                        else:
                            rotate[i+1] = 2
                    if rotate[i-1] == 0:
                        if not left_check(i):
                            rotate[i-1] = -rotate[i]
                        else:
                            rotate[i-1] = 2

    return rotate


def calc():
    global result

    for idx, t in enumerate(table):
        if t[0] == 1:
            if idx == 0:
                result += 1
            elif idx == 1:
                result += 2
            elif idx == 2:
                reult += 4
            else:
                result += 8


table = [deque(map(int, input())) for _ in range(4)]
k = int(input())
result = 0
for _ in range(k):
    n, d = map(int, input().split())
    r_dir = rotate_dir()
    for idx, t in enumerate(table):
        if r_dir[idx] == 2:
            continue
        else:
            t.rotate(r_dir[idx])

calc()

print(result)