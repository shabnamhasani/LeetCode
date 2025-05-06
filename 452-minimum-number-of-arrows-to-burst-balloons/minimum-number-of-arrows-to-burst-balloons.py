class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # Sort based on end coordinate
        points.sort(key=lambda x: x[1])
        arrow,curEnd=1,points[0][1]
        for start,end in points[1:]:
            if start > curEnd:
                arrow +=1
                curEnd=end
        return arrow