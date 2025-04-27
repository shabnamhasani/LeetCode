from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # counter_t = Counter(t)
        # for char in s:
        #     if char not in counter_t or counter_t[char]==0:
        #         return False
        #     counter_t[char] -=1
        # return True
        return Counter(s) == Counter(t)
        