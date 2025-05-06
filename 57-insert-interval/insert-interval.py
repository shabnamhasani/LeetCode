class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #O(nlog(n))
        # intervals.append(newInterval)
        # intervals.sort()
        # merged=[]
        # for i in range(len(intervals)):
        #     if merged ==[]:
        #         merged.append(intervals[i])
        #     else:
        #         previous_end=merged[-1][1]
        #         current_start=intervals[i][0]
        #         current_end=intervals[i][1]
        #         if previous_end >=current_start:
        #             merged[-1][1]=max(previous_end, current_end)
        #         else:
        #             merged.append(intervals[i])
        # return merged

        # 1. Add all intervals that come before newInterval
        # 2. Merge overlapping intervals with newInterval
        merged=[]
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif newInterval[1] < interval[0]:
                merged.append(newInterval)
                return merged + intervals[i:]
            else: 
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        merged.append(newInterval)
        return merged

