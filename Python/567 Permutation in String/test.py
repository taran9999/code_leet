from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        sol = solution(s1, s2)
        self.assertTrue(sol)

    def test_example2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        sol = solution(s1, s2)
        self.assertTrue(not sol)

    def test_fail1(self):
        s1 = "adc"
        s2 = "dcda"
        sol = solution(s1, s2)
        self.assertTrue(sol)


if __name__ == '__main__':
    main()
