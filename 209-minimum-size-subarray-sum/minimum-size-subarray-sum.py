import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """sliding window implemented by 2 pointers"""
        # min_len=float('inf')
        # left,total=0,0

        # for right in range(len(nums)):
        #     total +=nums[right]

        #     while (total >=target):
        #         min_len=min(min_len,right-left+1)
        #         total -=nums[left]
        #         left +=1

        # return 0 if min_len==float('inf') else min_len
        """binary search + prefix sum"""
        n=len(nums)
        min_len=float('inf')
        prefix=[0]*(n+1)
        # Step 1: Build prefix sum array
        for i in range (n):
            prefix[i+1]=prefix[i]+nums[i]

        # Step 2: For each i, binary search the smallest j where prefix[j] >= prefix[i] + target
        for i in range(n):
            required=prefix[i] + target
            # Binary search for the smallest index j where prefix[j] >= required
            #With slicing (prefix[i:]), Python creates a copy of part of the list 
            bound= bisect.bisect_left(prefix, required)
            if bound <=n:
                min_len=min(min_len, bound-i)
        return 0 if min_len ==float('inf') else min_len




