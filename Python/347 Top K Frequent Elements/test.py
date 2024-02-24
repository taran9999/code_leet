from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        output = [1, 2]
        sol = solution(nums, k)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums = [1]
        k = 1
        output = [1]
        sol = solution(nums, k)
        self.assertEqual(output, sol)

    def test_fail1(self):
        nums = [4, 1, -1, 2, -1, 2, 3]
        k = 2
        output = [-1, 2]
        sol = solution(nums, k)
        self.assertEqual(sorted(output), sorted(sol))

    def test_fail2(self):
        nums = [5, 3, 1, 1, 1, 3, 73, 1]
        k = 2
        output = [1, 3]
        sol = solution(nums, k)
        self.assertEqual(sorted(output), sorted(sol))

    def test_fail3(self):
        nums = [5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3]
        k = 3
        output = [3, 7, 10]
        sol = solution(nums, k)
        self.assertEqual(sorted(output), sorted(sol))


if __name__ == '__main__':
    main()
