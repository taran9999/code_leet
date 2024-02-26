from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [100, 4, 200, 1, 3, 2]
        output = 4
        sol = solution(nums)
        self.assertEqual(sol, output)

    def test_example2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        output = 9
        sol = solution(nums)
        self.assertEqual(sol, output)


if __name__ == '__main__':
    main()
