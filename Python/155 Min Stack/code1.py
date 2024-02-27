class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if len(self.stack) > 0:
            curr_min_index = self.stack[-1][1]
            if val < self.stack[curr_min_index][0]: self.stack.append((val, len(self.stack)))
            else: self.stack.append((val, curr_min_index))
        else: self.stack.append((val, 0))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        min_index = self.stack[-1][1]
        return self.stack[min_index][0]

