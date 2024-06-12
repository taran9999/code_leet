from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        piles = [3, 6, 7, 11]
        h = 8
        output = 4
        sol = solution(piles, h)
        self.assertEqual(output, sol)

    def test_example2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        output = 30
        sol = solution(piles, h)
        self.assertEqual(output, sol)

    def test_example3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        output = 23
        sol = solution(piles, h)
        self.assertEqual(output, sol)

    def test_fail1(self):
        piles = [312884470]
        h = 312884469
        output = 2
        sol = solution(piles, h)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
