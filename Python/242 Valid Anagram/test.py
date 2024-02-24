from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        sol = solution("anagram", "nagaram")
        self.assertTrue(sol)

    def test_example2(self):
        sol = solution("rat", "car")
        self.assertFalse(sol)


if __name__ == '__main__':
    main()
