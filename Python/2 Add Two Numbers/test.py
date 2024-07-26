from code1 import solution, ListNode
from unittest import TestCase, main


def create_linked_list(ls: list):
    head = None
    prev_node = None

    for e in ls:
        node = ListNode(val=e)
        if not head:
            head = node
        elif prev_node:
            prev_node.next = node
        prev_node = node

    return head


def convert_to_list(head: ListNode):
    if not head: return []

    ls = []
    curr = head
    while curr:
        ls.append(curr.val)
        curr = curr.next

    return ls


class TestCases(TestCase):
    def test_example1(self):
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        output = [7, 0, 8]
        sol = convert_to_list(solution(l1, l2))
        self.assertEqual(output, sol)

    def test_example2(self):
        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        output = [0]
        sol = convert_to_list(solution(l1, l2))
        self.assertEqual(output, sol)

    def test_example3(self):
        l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = create_linked_list([9, 9, 9, 9])
        output = [8, 9, 9, 9, 0, 0, 0, 1]
        sol = convert_to_list(solution(l1, l2))
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
