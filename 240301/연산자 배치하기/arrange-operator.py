def calulate(num1, num2, operator):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    else:
        return num1 * num2


def dfs(cnt, val):
    global min_result, max_result

    if cnt == n - 1:
        min_result = min(min_result, val)
        max_result = max(max_result, val)
        return
    
    for i in range(3):
        if operators_cnt[i]:
            operators_cnt[i] -= 1
            dfs(cnt+1, calulate(val, nums[cnt+1], i))
            operators_cnt[i] += 1


n = int(input())
nums = list(map(int, input().split()))
operators_cnt = list(map(int, input().split()))
min_result, max_result = int(1e9), int(-1e9)

dfs(0, nums[0])
print(min_result, max_result)