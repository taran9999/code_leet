from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        sol = solution(s, t)
        self.assertEqual(output, sol)

    def test_example2(self):
        s = "a"
        t = "a"
        output = "a"
        sol = solution(s, t)
        self.assertEqual(output, sol)

    def test_example3(self):
        s = "a"
        t = "aa"
        output = ""
        sol = solution(s, t)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
