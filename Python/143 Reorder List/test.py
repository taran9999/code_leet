from code2 import solution, ListNode
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
        input_list = [1, 2, 3, 4]
        output = [1, 4, 2, 3]
        head = create_linked_list(input_list)
        solution(head)
        sol = convert_to_list(head)
        self.assertEqual(output, sol)

    def test_example2(self):
        input_list = [1, 2, 3, 4, 5]
        output = [1, 5, 2, 4, 3]
        head = create_linked_list(input_list)
        solution(head)
        sol = convert_to_list(head)
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
