class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """The solution structure is similar, but in #80, you need a counter or a condition 
        to allow a second occurrence before skipping duplicates."""
        if not nums:
            return 0  # Edge case: empty list
        p1,p2,count=0,1,1
        while p2<len(nums):
            if (nums[p1]!=nums[p2]):
                p1 +=1
                nums[p1]=nums[p2]
                count =1
            elif count <2:
                count +=1
                p1 +=1
                nums[p1]=nums[p2]

            p2 +=1
        return p1+1



        