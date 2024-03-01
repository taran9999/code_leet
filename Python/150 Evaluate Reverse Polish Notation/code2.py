def solution(tokens):
    stack = []
    for token in tokens:
        if token == '+': stack.append(stack.pop() + stack.pop())
        elif token == '*': stack.append(stack.pop() * stack.pop())
        elif token == '-':
            op1, op2 = stack.pop(), stack.pop()
            stack.append(op2 - op1)
        elif token == '/':
            op1, op2 = stack.pop(), stack.pop()
            stack.append(int(op2 / op1))
        else:
            stack.append(int(token))

    return stack[0]
