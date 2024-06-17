class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    curr = head
    prev = None
    while curr:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t
    return prev
