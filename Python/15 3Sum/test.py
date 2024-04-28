from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        sol = solution(nums)
        self.assertEqual(sorted(output), sorted(sol))

    def test_example2(self):
        nums = [0, 1, 1]
        output = []
        sol = solution(nums)
        self.assertEqual(sorted(output), sorted(sol))

    def test_example3(self):
        nums = [0, 0, 0]
        output = [[0, 0, 0]]
        sol = solution(nums)
        self.assertEqual(sorted(output), sorted(sol))

    def test_fail1(self):
        nums = [0, 0, 0, 0]
        output = [[0, 0, 0]]
        sol = solution(nums)
        self.assertEqual(sorted(output), sorted(sol))

    def test_fail2(self):
        nums = [-2, 0, 1, 1, 2]
        output = [[-2, 0, 2], [-2, 1, 1]]
        sol = solution(nums)
        self.assertEqual(sorted(output), sorted(sol))


if __name__ == '__main__':
    main()
