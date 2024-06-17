class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(list1, list2):

    def min_node(n1, n2):
        if n1 and n2:
            if n1.val < n2.val:
                t = n1
                n1 = n1.next
            else:
                t = n2
                n2 = n2.next
        elif n1:
            t = n1
            n1 = n1.next
        elif n2:
            t = n2
            n2 = n2.next
        else:
            t = None

        return t, n1, n2

    head, list1, list2 = min_node(list1, list2)
    curr = head
    while curr:
        curr.next, list1, list2 = min_node(list1, list2)
        curr = curr.next
    return head


