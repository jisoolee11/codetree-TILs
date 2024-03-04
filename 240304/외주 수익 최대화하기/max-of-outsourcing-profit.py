n = int(input())

time_profits = [tuple(map(int, input().split())) for _ in range(n)]
times = [(i, i+time-1) for i, (time, _) in enumerate(time_profits, start=1)]
profits = [profit for _, profit in time_profits]

selected_jobs = []
max_profit = 0


def get_profit():
    return sum([
        profits[job_idx]
        for job_idx in selected_jobs
    ])


def is_available():
    if len(selected_jobs) > 1:
        _, end_time = times[selected_jobs[-2]]
        start_time, _ = times[selected_jobs[-1]]
        if end_time >= start_time:
            return False
    
    _, end_time = times[selected_jobs[-1]]

    if end_time > n:
        return False

    return True


def find_max_profit(curr_idx):
    global max_profit
    
    if curr_idx == n:
        max_profit = max(max_profit, get_profit())
        return
    
    find_max_profit(curr_idx + 1)
    
    selected_jobs.append(curr_idx)
    if is_available():
        find_max_profit(curr_idx + 1)
    selected_jobs.pop()
    

find_max_profit(0)
print(max_profit)