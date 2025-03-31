class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """Boyer-Moore Voting Algorithm"""
        """Using a Hash Map (Dictionary) to Find the Majority Element"""
        col={}
        for num in nums:
            col[num] = col.get(num, 0) + 1  # Increment count
            if col[num]> len(nums) //2:
                return num


        