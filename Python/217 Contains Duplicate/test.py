from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        self.assertTrue(solution([1, 2, 3, 1]))

    def test_example2(self):
        self.assertFalse(solution([1, 2, 3, 4]))

    def test_example3(self):
        self.assertTrue(solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    main()
