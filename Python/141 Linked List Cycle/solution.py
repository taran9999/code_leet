
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()
        while head is not None:
            seen_nodes.add(head)
            if head.next in seen_nodes: return True
            head = head.next
        return False
