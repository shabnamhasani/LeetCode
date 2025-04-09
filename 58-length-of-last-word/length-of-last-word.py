class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """After trimming the end, start iterating backward. The moment you hit a space, you know the last word has ended, and you can stop counting."""
        s=rstrip(s)
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                count+=1
            else:
                break
        return count
            