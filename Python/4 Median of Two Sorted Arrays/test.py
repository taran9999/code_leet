from code1 import solution
from unittest import TestCase, main


class TestCases(TestCase):
    def test_example1(self):
        nums1 = [1, 3]
        nums2 = [2]
        output = 2.0
        sol = solution(nums1, nums2)
        self.assertEqual(output, sol)

    def test_example2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        output = 2.5
        sol = solution(nums1, nums2)
        self.assertEqual(output, sol)

    def test_custom1(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [3, 4, 5]
        output = 3.0
        sol = solution(nums1, nums2)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
