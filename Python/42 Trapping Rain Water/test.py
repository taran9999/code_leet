from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        output = 6
        sol = solution(height)
        self.assertEqual(output, sol)

    def test_example2(self):
        height = [4, 2, 0, 3, 2, 5]
        output = 9
        sol = solution(height)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
