class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted_array=np.sort(nums)
        nums.sort()  # Use built-in sort
        output=[]
        for i,item in enumerate(nums):
            if i > 0 and item == nums[i - 1]:
                continue  # Skip duplicates for the fixed element
            p1,p2=i+1,len(nums)-1
            while(p1<p2):
                sum=item+nums[p1]+nums[p2]
                if (sum==0):
                    output.append([item, nums[p1], nums[p2]])
                    p1 +=1
                    p2 -=1
                    while(p1<p2 and nums[p1]==nums[p1-1]):
                       p1 +=1
                    while (p1<p2 and nums[p2]==nums[p2+1]):
                       p2 -=1
                elif sum<0:
                    p1 +=1
                else:
                    p2 -=1
        return output

