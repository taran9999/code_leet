from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        output = [1, 2]
        sol = solution(numbers, target)
        self.assertEqual(sorted(output), sorted(sol))

    def test_example2(self):
        numbers = [2, 3, 4]
        target = 6
        output = [1, 3]
        sol = solution(numbers, target)
        self.assertEqual(sorted(output), sorted(sol))

    def test_example3(self):
        numbers = [-1, 0]
        target = -1
        output = [1, 2]
        sol = solution(numbers, target)
        self.assertEqual(sorted(output), sorted(sol))


if __name__ == '__main__':
    main()
