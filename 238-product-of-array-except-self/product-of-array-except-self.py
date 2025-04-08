class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """In the first pass, compute prefix products and store them in the output array.
        In the second pass, go backwards to multiply suffix products into the output array."""
        n = len(nums)
        output = [1] * n  # Initialize the output array with 1s
        prefix=1
        for i in range(n):
            output[i]=prefix
            prefix *=nums[i]
        suffix=1
        for i in range(n-1, -1, -1):
            output[i] *=suffix
            suffix *=nums[i]
        return output
 