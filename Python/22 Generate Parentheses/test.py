from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        n = 3
        output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        sol = solution(n)
        self.assertEqual(sorted(output), sorted(sol))

    def test_example2(self):
        n = 1
        output = ["()"]
        sol = solution(n)
        self.assertEqual(sorted(output), sorted(sol))


if __name__ == '__main__':
    main()
