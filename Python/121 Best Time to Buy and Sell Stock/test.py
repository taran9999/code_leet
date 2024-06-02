from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        output = 5
        sol = solution(prices)
        self.assertEqual(output, sol)

    def test_example2(self):
        prices = [7, 6, 4, 3, 1]
        output = 0
        sol = solution(prices)
        self.assertEqual(output, sol)

    def test_fail1(self):
        prices = [2, 4, 1]
        output = 2
        sol = solution(prices)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
