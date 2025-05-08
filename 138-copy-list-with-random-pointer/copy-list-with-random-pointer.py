"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Clone each node and insert it just after the original node
        current=head
        while (current):
            copy=Node(current.val,current.next)
            current.next=copy
            current=copy.next
        # Step 2: Assign random pointers for the cloned nodes
        current=head
        while (current):
            if current.random:
                current.next.random=current.random.next
            current=current.next.next

        # Step 3: Restore the original list and extract the cloned list
        current = head
        copy_head = head.next
        copy_current = copy_head

        while current:
            current.next = copy_current.next
            current = current.next
            if current:
                copy_current.next = current.next
                copy_current = copy_current.next

        return copy_head

        