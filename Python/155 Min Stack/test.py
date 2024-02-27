from code1 import MinStack
from unittest import TestCase, main


def get_output(commands, params):
    output = []
    stack = None
    for i in range(len(commands)):
        if commands[i] == "MinStack":
            stack = MinStack()
            output.append(None)
        elif commands[i] == "push":
            val = params[i][0]
            stack.push(val)
            output.append(None)
        elif commands[i] == "pop":
            stack.pop()
            output.append(None)
        elif commands[i] == "top":
            val = stack.top()
            output.append(val)
        elif commands[i] == "getMin":
            val = stack.getMin()
            output.append(val)

    return output


class TestCases(TestCase):
    def test_example1(self):
        commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
        params = [[], [-2], [0], [-3], [], [], [], []]
        out = get_output(commands, params)
        output = [None, None, None, None, -3, None, 0, -2]
        self.assertEqual(out, output)

    def test_fail1(self):
        commands = ["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin"]
        params = [[], [-2], [0], [-1], [], [], [], []]
        out = get_output(commands, params)
        output = [None, None, None, None, -2, -1, None, -2]
        self.assertEqual(out, output)


if __name__ == '__main__':
    main()
