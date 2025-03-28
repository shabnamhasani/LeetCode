class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1,p2=0,0
        while p1<(len(nums)):
            if nums[p1]==val:
                p1 +=1
            else:
                nums[p2]=nums[p1]
                p1 +=1
                p2 +=1
        return p2

         
            