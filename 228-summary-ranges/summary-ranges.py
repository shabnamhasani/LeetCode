class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        output=[]
        start=nums[0]

        for i in range(1,len(nums)):
            #Check if current number is not consecutive
            if nums[i] != nums[i-1] + 1:
                end=nums[i-1]
                if start==end:
                    output.append(f"{start}")
                else:
                    output.append(f"{start}->{end}")
                start=nums[i]
        # Add the final range
        end = nums[-1]
        if start == end:
            output.append(f"{start}")
        else:
            output.append(f"{start}->{end}")

        return output
