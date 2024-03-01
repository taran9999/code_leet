from code2 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        tokens = ["2", "1", "+", "3", "*"]
        sol = solution(tokens)
        self.assertEqual(9, sol)

    def test_example2(self):
        tokens = ["4", "13", "5", "/", "+"]
        sol = solution(tokens)
        self.assertEqual(6, sol)

    def test_example3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        sol = solution(tokens)
        self.assertEqual(22, sol)

    def test_fail1(self):
        tokens = ["18"]
        sol = solution(tokens)
        self.assertEqual(18, sol)

if __name__ == '__main__':
    main()
