# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""Record the queue size (number of nodes at that level).
Loop that many times, popping one node at a time, summing its value, and enqueuing its children.
Divide the sum by the level size to get the average, and store it."""
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result=[]
        queue=deque([root])

        while queue:
            level_count=len(queue)
            level_sum=0

            for _ in range(level_count):
                node=queue.popleft()
                level_sum +=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(level_sum/level_count)
        return result

        