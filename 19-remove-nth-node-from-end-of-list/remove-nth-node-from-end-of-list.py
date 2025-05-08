# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First pass: count the total number of nodes
        length=0
        if not head:
            return None
        current=head
        while (current):
            current=current.next
            length +=1
        # If we want to remove the head
        if n==length: 
            return head.next
        # Second pass: go to the node before the one to delete
        current = head
        for _ in range(length - n - 1):
            current = current.next

        # Delete the node
        current.next = current.next.next
        return head