from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Does any substring of s2 (of length equal to s1) have the same character counts as s1"""
        hash_map=defaultdict(int)
        #create hash map of S1
        # for i, k in enumerate(s1):
        #     hash_map[k] +=1
        cntr,w=Counter(s1),len(s1)
        for i in range (len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -=1
            """When the window size exceeds w, we slide the window forward.
            So, we add back the character that just went out of the window (i.e., at i - w).
            Why? Because cntr needs to reflect only the current window of length w"""
            if i >=w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1
            if all([cntr[i] == 0 for i in cntr]): 
                return True

        return False
