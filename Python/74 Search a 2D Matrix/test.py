from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        sol = solution(matrix, target)
        self.assertTrue(sol)

    def test_example2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        sol = solution(matrix, target)
        self.assertFalse(sol)


if __name__ == '__main__':
    main()
