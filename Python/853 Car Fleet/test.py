from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        output = 3
        sol = solution(target, position, speed)
        self.assertEqual(output, sol)

    def test_example2(self):
        target = 10
        position = [3]
        speed = [3]
        output = 1
        sol = solution(target, position, speed)
        self.assertEqual(output, sol)

    def test_example3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        output = 1
        sol = solution(target, position, speed)
        self.assertEqual(output, sol)

    def test_fail1(self):
        target = 20
        position = [2, 6, 5, 13, 19, 18, 1, 12, 10, 16, 4, 11]
        speed = [6, 1, 10, 3, 1, 5, 9, 7, 9, 2, 8, 3]
        output = 5
        sol = solution(target, position, speed)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
