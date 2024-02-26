n = int(input())
num = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
operators = []
min_result, max_result = 1e9, -1e9

def calculate():
    val = num[0]
    for i, operator in enumerate(operators):
        if operator == 0:
            val += num[i+1]
        elif operator == 1:
            val -= num[i+1]
        else:
            val *= num[i+1]

    return val


def find_result(cnt):
    global min_result, max_result

    if cnt == n - 1:
        val = calculate()
        min_result = min(min_result, val)
        max_result = max(max_result, val)

        return

    for i in range(3):
        if operator_cnt[i]:
            operators.append(i)
            operator_cnt[i] -= 1

            find_result(cnt+1)

            operators.pop()
            operator_cnt[i] += 1


find_result(0)
print(min_result, max_result)