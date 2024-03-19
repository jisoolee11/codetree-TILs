from collections import Counter

def row(A):
    new_A = []
    max_length = 0
    for a in A:
        while 0 in a:
            a.remove(0)

    for a in A:
        new_a = []
        sorted_a = sorted(Counter(a).items(), key = lambda x: (x[1], x[0]))
        for s in sorted_a:
            new_a.extend(s)
        max_length = max(max_length, len(new_a))
        new_A.append(new_a)

    zfill_A = []
    for nA in new_A:
        zfill_A.append(nA + [0]*(max_length-len(nA)))

    return zfill_A


def rotate_90(A):
    new_A = [[0] * len(A) for _ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            new_A[j][len(A)-i-1] = A[i][j]

    return new_A


def rotate_270(A):
    new_A = [[0] * len(A) for _ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            new_A[len(A[0])-j-1][i] = A[i][j]

    for nA in new_A:
        while 0 in nA:
            nA.remove(0)

    new_A = row(new_A)
    origin_A = rotate_90(new_A)

    return origin_A

        
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
t = 0

while True:
    if r <= len(A) and c <= len(A[0]):
        if A[r-1][c-1] == k:
            print(t)
            break

    if len(A) >= len(A[0]):
        A = row(A)
    else:
        A = rotate_270(A)

    t += 1