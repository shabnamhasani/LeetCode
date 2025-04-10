class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack) - len(needle) + 1): #checking substrings of haystack starting at position i with length len(needle). So if you go too far, you'd go out of bounds.
            if haystack[i:i+len(needle)].startswith(needle):
                return i
        return -1

        