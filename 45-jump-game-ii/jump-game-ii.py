class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """at each jump, choose the option that lets you go the farthest within your current jump window, and only jump when that window ends."""

        """Input: [2,3,1,1,4]
        Start at index 0, can jump to index 2 → farthest = 2
        At index 1, can reach index 4 → farthest = 4
        At index 2, farthest remains 4, but we must jump (since we reached current_end).
        From index 1 → Jump to index 4 (final position).
        Output: 2 (Jumps: index 0 → 1 → 4)"""

        farthest,jump_counter,current_end=0,0,0
        # The end of the current jump window: current_end
        # The farthest index we can reach: farthest
        # Number of jumps made: jump_counter
        if len(nums)==1:
            return 0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if (i==current_end):
                jump_counter +=1
                current_end=farthest
        return jump_counter

            

        