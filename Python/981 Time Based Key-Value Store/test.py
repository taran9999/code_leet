from code1 import TimeMap
from unittest import TestCase, main


def get_output(commands, params):
    output = []
    kv = None
    for i in range(len(commands)):
        if commands[i] == "TimeMap":
            kv = TimeMap()
            output.append(None)
        elif commands[i] == "set":
            key = params[i][0]
            value = params[i][1]
            timestamp = params[i][2]
            kv.set(key, value, timestamp)
            output.append(None)
        elif commands[i] == "get":
            key = params[i][0]
            timestamp = params[i][1]
            val = kv.get(key, timestamp)
            output.append(val)
    return output


class TestCases(TestCase):
    def test_example1(self):
        commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
        params = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
        out = get_output(commands, params)
        output = [None, None, "bar", "bar", None, "bar2", "bar2"]
        self.assertEqual(output, out)


if __name__ == '__main__':
    main()
