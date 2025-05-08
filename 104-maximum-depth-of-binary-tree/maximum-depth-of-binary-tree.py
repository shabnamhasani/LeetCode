#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: empty tree has depth 0
        # Recursive case: 1 (for current node) + max depth of left or right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))