from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        sol = solution(s)
        self.assertTrue(sol)

    def test_example2(self):
        s = "race a car"
        sol = solution(s)
        self.assertFalse(sol)

    def test_example3(self):
        s = " "
        sol = solution(s)
        self.assertTrue(sol)


if __name__ == '__main__':
    main()
