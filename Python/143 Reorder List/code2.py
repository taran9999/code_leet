class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# better solution, order is first half and reversed second half while interchanging elements
# [1, 2, 3, 4, 5] -> [1, 2, 3] + [5, 4] => [1, 5, 2, 4, 3]
def solution(head):
    # slow/fast trick to find middle (p1 will point to mid-element)
    if head is None: return
    p1, p2 = head, head
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next

    # reverse the second half
    # [1, 2, 3, 4, 5] -> [1, 2, 3, 5, 4]
    prev, curr = None, p1.next
    while curr:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t
    p1.next = None  # mid element becomes last element

    # head = original head, prev = start or reversed second half

    # merge the twp halves
    p1 = head
    p2 = prev
    while p2:
        first_next = p1.next
        p1.next = p2
        p1 = p2
        p2 = first_next
