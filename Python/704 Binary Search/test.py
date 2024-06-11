from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        output = 4
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        output = -1
        sol = solution(nums, target)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
