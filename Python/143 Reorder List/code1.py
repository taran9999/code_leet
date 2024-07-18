class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    second = head.next
    if head is not None and second is not None and second.next is not None:
        tail_prev = head
        while tail_prev.next.next is not None: tail_prev = tail_prev.next
        tail = tail_prev.next
        head.next = tail
        tail.next = second
        tail_prev.next = None
        solution(second)

