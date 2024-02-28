def get_profit():
    sum_profit = 0
    for idx in selected_task:
        sum_profit += profits[idx]
    return sum_profit


def is_available():
    for i in range(len(selected_task)-1):
        _, end_time = times[selected_task[i]]
        start_time, _ = times[selected_task[i+1]]
        if end_time >= start_time:
            return False

    for idx in selected_task:
        _, end_time = times[idx]
        if end_time > n:
            return False

    return True


def find_max_profit(cur_idx):
    global max_result

    if cur_idx == n:
        if is_available():
            max_result = max(max_result, get_profit())
        return

    find_max_profit(cur_idx+1)

    selected_task.append(cur_idx)
    find_max_profit(cur_idx+1)
    selected_task.pop()


n = int(input())
task = []
for _ in range(n):
    t, p = map(int, input().split())
    task.append((t, p))

times = []
for i, (time, _) in enumerate(task, start=1):
    times.append((i, i+time-1))

profits = []
for _, profit in task:
    profits.append(profit)


selected_task = []
max_result = 0

find_max_profit(0)
print(max_result)