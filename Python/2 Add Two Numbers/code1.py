class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1, l2):
    s = l1.val + l2.val
    curr = r = ListNode(s % 10, None)
    carry = s // 10
    l1 = l1.next
    l2 = l2.next

    while l1 is not None and l2 is not None:
        s = l1.val + l2.val + carry
        curr.next = ListNode(s % 10, None)
        curr = curr.next
        carry = s // 10
        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        s = l1.val + carry
        curr.next = ListNode(s % 10, None)
        curr = curr.next
        carry = s // 10
        l1 = l1.next

    while l2 is not None:
        s = l2.val + carry
        curr.next = ListNode(s % 10, None)
        curr = curr.next
        carry = s // 10
        l2 = l2.next

    if carry: curr.next = ListNode(1, None)

    return r

