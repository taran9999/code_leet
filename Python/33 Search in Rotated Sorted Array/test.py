from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        output = 4
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        output = -1
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_example3(self):
        nums = [1]
        target = 0
        output = -1
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_fail1(self):
        nums = [1, 3]
        target = 3
        output = 1
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_fail2(self):
        nums = [1, 3, 5]
        target = 5
        output = 2
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_custom1(self):
        nums = [3, 4, 5, 1, 2]
        target = 1
        output = 3
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_fail3(self):
        nums = [5, 1, 3]
        target = 5
        output = 0
        sol = solution(nums, target)
        self.assertEqual(output, sol)

    def test_fail4(self):
        nums = [4, 5, 6, 7, 8, 1, 2, 3]
        target = 8
        output = 4
        sol = solution(nums, target)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
