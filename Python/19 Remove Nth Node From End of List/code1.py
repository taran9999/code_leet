class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head, n):
    # two pointer counter, p1 will move to nth from last
    p1 = head
    p2 = head
    p1_prev = None
    for i in range(n): p2 = p2.next
    while p2 is not None:
        p1_prev = p1
        p1 = p1.next
        p2 = p2.next

    # skip p1
    if p1_prev: p1_prev.next = p1.next
    else: return p1.next  # p1 is head
    return head

