# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""A height-balanced BST is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than 1. Since the array is sorted, the middle element naturally becomes the root to maintain balance."""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])     # left half
        root.right = self.sortedArrayToBST(nums[mid+1:])  # right half
        return root
