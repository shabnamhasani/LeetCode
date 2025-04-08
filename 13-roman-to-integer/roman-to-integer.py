class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """reverse iteration + compare previous value one"""
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  
        previous,total=0,0
        for i in range(len(s)-1, -1,-1):
            value=roman[s[i]]
            if value<previous:
                total -=value
            else:
                total +=value
            previous=value
        return total


