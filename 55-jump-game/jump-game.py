class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gas=0
        for value in nums:
            if (gas<0):
                return False
            elif value>gas:
                gas= value
            gas -=1
        return True