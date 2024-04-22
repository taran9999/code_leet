from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        heights = [2, 1, 5, 6, 2, 3]
        output = 10
        sol = solution(heights)
        self.assertEqual(output, sol)

    def test_example2(self):
        heights = [2, 4]
        output = 4
        sol = solution(heights)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
