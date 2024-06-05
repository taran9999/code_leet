from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        s = "abcabcbb"
        output = 3
        sol = solution(s)
        self.assertEqual(output, sol)

    def test_example2(self):
        s = "bbbbb"
        output = 1
        sol = solution(s)
        self.assertEqual(output, sol)

    def test_example3(self):
        s = "pwwkew"
        output = 3
        sol = solution(s)
        self.assertEqual(output, sol)

if __name__ == '__main__':
    main()
