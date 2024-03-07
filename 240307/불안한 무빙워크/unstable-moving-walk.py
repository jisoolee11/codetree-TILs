from collections import deque


def person_remove():
    if n-1 in person:
        person.remove(n-1)


def moving_rotate():
    moving_safe.rotate()
    for i in range(len(person)):
        person[i] += 1

    person_remove()


def moving_person():
    for idx, i in enumerate(person):
        if i+1 not in person and moving_safe[i+1] != 0:
            person[idx] = i+1
            moving_safe[i+1] -= 1

    person_remove()


def new_person():
    if 0 not in person and moving_safe[0] != 0:
        person.append(0)
        moving_safe[0] -= 1

    person_remove()


n, k = map(int, input().split())
moving_safe = deque(map(int, input().split()))
person = []

cnt = 0
while moving_safe.count(0) < k:
    cnt += 1
    moving_rotate()
    moving_person()
    new_person()

print(cnt)