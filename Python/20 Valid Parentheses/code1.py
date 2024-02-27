def solution(s):
    stack = []

    for c in s:
        if c == '(' or c == '[' or c == '{': stack.append(c)
        else:
            if stack:
                if c == ')' and stack[-1] == '(': stack.pop()
                elif c == ']' and stack[-1] == '[': stack.pop()
                elif c == '}' and stack[-1] == '{': stack.pop()
                else: return False
            else: return False

    return not stack

