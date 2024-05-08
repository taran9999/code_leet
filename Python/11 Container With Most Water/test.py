from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        sol = solution(height)
        self.assertEqual(output, sol)

    def test_example2(self):
        height = [1, 1]
        output = 1
        sol = solution(height)
        self.assertEqual(output, sol)

    def test_fail1(self):
        height = [1, 2, 4, 3]
        output = 4
        sol = solution(height)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
