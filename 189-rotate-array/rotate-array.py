class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """Copy the last k elements to a temporary array.
        Shift the remaining elements k places to the right (iterate from the back).
        Copy the stored k elements to the front.   """
        n = len(nums)
        k = k % n  # Handle cases where k > n
        temp=[]
        
        # Step 1: Copy last k elements
        for i in range(n-k,n,1):
            temp.append(nums[i])
        # Step 2: Shift elements k places to the right
        for i in range(n - k - 1, -1, -1):  # Iterate backwards
            nums[i+k]=nums[i]
        # Step 3: Place temp elements at the start
        for i in range(k):
            nums[i]=temp[i]



        