from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        s = "ABAB"
        k = 2
        output = 4
        sol = solution(s, k)
        self.assertEqual(output, sol)

    def test_example2(self):
        s = "AABABBA"
        k = 1
        output = 4
        sol = solution(s, k)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
