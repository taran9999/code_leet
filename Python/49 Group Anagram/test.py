from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        sol = solution(strs)
        self.assertCountEqual([sorted(inner_list) for inner_list in output], [sorted(inner_list) for inner_list in sol])

    def test_example2(self):
        strs = [""]
        output = [[""]]
        sol = solution(strs)
        self.assertCountEqual([sorted(inner_list) for inner_list in output], [sorted(inner_list) for inner_list in sol])

    def test_example3(self):
        strs = ["a"]
        output = [["a"]]
        sol = solution(strs)
        self.assertCountEqual([sorted(inner_list) for inner_list in output], [sorted(inner_list) for inner_list in sol])


if __name__ == '__main__':
    main()
