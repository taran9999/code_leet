from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        output = [24, 12, 8, 6]
        sol = solution(nums)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        output = [0, 0, 9, 0, 0]
        sol = solution(nums)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
