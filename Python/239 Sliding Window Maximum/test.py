from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        output = [3, 3, 5, 5, 6, 7]
        sol = solution(nums, k)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums = [1]
        k = 1
        output = [1]
        sol = solution(nums, k)
        self.assertEqual(output, sol)

    def test_fail1(self):
        nums = [1, -1]
        k = 1
        output = [1, -1]
        sol = solution(nums, k)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
