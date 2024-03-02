from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        output = [1, 1, 4, 2, 1, 1, 0, 0]
        sol = solution(temperatures)
        self.assertEqual(output, sol)

    def test_example2(self):
        temperatures = [30, 40, 50, 60]
        output = [1, 1, 1, 0]
        sol = solution(temperatures)
        self.assertEqual(output, sol)

    def test_example3(self):
        temperatures = [30, 60, 90]
        output = [1, 1, 0]
        sol = solution(temperatures)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
