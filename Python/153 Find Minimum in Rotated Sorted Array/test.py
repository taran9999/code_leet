from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [3, 4, 5, 1, 2]
        output = 1
        sol = solution(nums)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        output = 0
        sol = solution(nums)
        self.assertEqual(output, sol)

    def test_example3(self):
        nums = [11, 13, 15, 17]
        output = 11
        sol = solution(nums)
        self.assertEqual(output, sol)

    def test_custom1(self):
        nums = [3, 4, 5, 6, 7, 1, 2]
        output = 1
        sol = solution(nums)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
