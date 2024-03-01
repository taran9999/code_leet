def solution(tokens):
    # Use a buffer to store the values while we keep popping until seeing an operator, then two numbers
    # The first three values will be the two numbers and the operator
    # Evaluate and append result back on stack
    # append everything back on the stack and repeat

    buffer = []
    while len(tokens) > 1:
        while not (is_operator(tokens[-1]) and is_number(tokens[-2]) and is_number(tokens[-3])):
            val = tokens.pop()
            buffer.append(val)
        op = tokens.pop()
        op2 = int(tokens.pop())
        op1 = int(tokens.pop())
        if op == '+': tokens.append(op1 + op2)
        elif op == '-': tokens.append(op1 - op2)
        elif op == '*': tokens.append(op1 * op2)
        elif op == '/': tokens.append(int(op1 / op2))

        while len(buffer) > 0:
            val = buffer.pop()
            tokens.append(val)

    return int(tokens[0])

def is_operator(s):
    return s == '+' or s == '-' or s == '*' or s == '/'

def is_number(s):
    return isinstance(s, int) or s.isnumeric() or (s[0] == '-' and s[1:].isnumeric())
