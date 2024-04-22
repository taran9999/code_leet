def solution(heights):
    stack = []
    largest = 0
    heights.append(0)  # automatically test everything remaining on the stack

    for i, val in enumerate(heights):
        if len(stack) == 0 or stack[-1][0] < val:
            stack.append((val, i))
        else:
            start = 0
            while len(stack) > 0 and stack[-1][0] >= val:
                height, start = stack.pop()
                area = height * (i - start)
                if area > largest: largest = area
            stack.append((val, start))
    return largest
