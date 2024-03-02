def solution(temperatures):
    stack = []
    ans = []

    for i in range(len(temperatures)):
        ans.append(0)
        while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
            # current day warmer than day on top of stack
            j = stack.pop()
            ans[j] = i - j # current day - day being popped = days between
        stack.append(i)
    return ans
