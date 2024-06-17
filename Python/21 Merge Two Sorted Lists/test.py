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
        input_list_1 = [1, 2, 4]
        input_list_2 = [1, 3, 4]
        head_1 = create_linked_list(input_list_1)
        head_2 = create_linked_list(input_list_2)
        output = [1, 1, 2, 3, 4, 4]
        sol = convert_to_list(solution(head_1, head_2))
        self.assertEqual(output, sol)

    def test_example2(self):
        input_list_1 = []
        input_list_2 = []
        head_1 = create_linked_list(input_list_1)
        head_2 = create_linked_list(input_list_2)
        output = []
        sol = convert_to_list(solution(head_1, head_2))
        self.assertEqual(output, sol)

    def test_example3(self):
        input_list_1 = []
        input_list_2 = [0]
        head_1 = create_linked_list(input_list_1)
        head_2 = create_linked_list(input_list_2)
        output = [0]
        sol = convert_to_list(solution(head_1, head_2))
        self.assertEqual(output, sol)


if __name__ == '__main__':
    main()
