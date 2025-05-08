# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        # Step 1: move `prev` to the node before `left`
        for i in range(left-1):
            prev=prev.next
        # Step 2: reverse sublist from `left` to `right`
        current=prev.next
        for i in range(right-left):
            temp = current.next              # Node to move
            current.next = temp.next         # Remove temp
            temp.next = prev.next            # Insert temp after prev
            prev.next = temp                 # Reconnect prev to temp

        return dummy.next