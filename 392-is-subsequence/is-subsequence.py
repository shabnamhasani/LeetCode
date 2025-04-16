# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i,j=0,0
#         while i< len(s) and j< len(t):
#             if (s[i]==t[j]):
#                 i +=1
            
#             j +=1
#         return (i==len(s))

from os import preadv
from collections import defaultdict
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Preprocess t into index map
        index_map = defaultdict(list)
        for i, ch in enumerate(t):
            index_map[ch].append(i)

        # Use binary search to check s
        prev_index = -1
        for ch in s:
            if ch not in index_map:
                return False
            pos_list = index_map[ch]
            idx = bisect.bisect_right(pos_list, prev_index)
            if idx == len(pos_list):
                return False
            prev_index = pos_list[idx]
        return True
