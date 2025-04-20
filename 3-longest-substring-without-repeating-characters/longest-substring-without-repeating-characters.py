class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """We use **while** to remove all duplicates because we don’t know how many times a character might be duplicated in the window."""
        # seen=set()
        # left,max_len=0,0
        # for right in range(len(s)):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left +=1
        #     seen.add(s[right])
        #     max_len =max(max_len, right-left +1)
        # return max_len

        """Using a dictionary allows us to remember the last index where a character was seen and jump the left pointer directly past that"""
        char_ind={}
        left,max_len=0,0
        for right in range(len(s)):
            if s[right] in char_ind and char_ind[s[right]]>=left:
                # Move left pointer to one after the previous occurrence
                left=char_ind[s[right]]+1
            # Update the character's index
            char_ind[s[right]]=right
            max_len =max(max_len, right-left +1)
        return max_len