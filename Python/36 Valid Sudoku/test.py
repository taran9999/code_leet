from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        sol = solution(board)
        self.assertTrue(sol)

    def test_example2(self):
        board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        sol = solution(board)
        self.assertFalse(sol)

    def test_fail1(self):
        board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
        sol = solution(board)
        self.assertTrue(sol)

    def test_fail2(self):
        board = [[".", ".", "5", ".", ".", ".", ".", ".", "."], ["1", ".", ".", "2", ".", ".", ".", ".", "."],
                 [".", ".", "6", ".", ".", "3", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["3", ".", "1", "5", "2", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "4", "."],
                 [".", ".", "6", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "9", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."]]
        sol = solution(board)
        self.assertFalse(sol)


if __name__ == '__main__':
    main()
