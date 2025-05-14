"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root  # current node at the current level

        while curr:
            dummy = Node(0)  # dummy head of the next level
            tail = dummy     # tail to build the next level's linked list

            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # move to next node in current level
            
            curr = dummy.next  # move to the first node in the next level

        return root
        