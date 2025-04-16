class Solution:
    def maxArea(self, height: List[int]) -> int:
        """You’re looking for a taller line to potentially increase the area, even though the width shrinks.
        the container can only hold water up to the height of the shorter line"""
        n=len(height)
        p1,p2,max_area=0,n-1,0
        
        while (p1<p2):
            max_area= max(max_area, min(height[p1],height[p2])*(p2-p1))
            if height[p1]<height[p2]:
                p1 +=1
            else: 
                p2 -=1
        return max_area
