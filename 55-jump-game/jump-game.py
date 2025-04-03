class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """gas=0
        for value in nums:
            if (gas<0):
                return False
            elif value>gas:
                gas= value
            gas -=1
        return True"""
        """Keep track of the farthest index you can reach.
        Iterate through the array, updating the farthest reachable index at each step.
        If at any index, the farthest reachable index is less than the current index, return False  (since you are stuck).
        If the farthest reachable index is greater than or equal to the last index, return True."""
        max_reachable,i=0,0
        for i in range(len(nums)): 
            if len(nums) == 1:
                return True  # Single-element array means we're already at the last index

            if (max_reachable < i):
                return False
            max_reachable=max(max_reachable,(i+nums[i]))
            if max_reachable >= len(nums) - 1:  # Early exit if we can reach the end
                return True
        return False
