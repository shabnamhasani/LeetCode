class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """Trim the input to remove leading and trailing spaces.
        Initialize a result list or string builder.
        Traverse the string backward:
        Skip extra spaces between words.
        Identify each word (sequence of non-space characters).
        Append the word to your result.
        Add a single space between words.
        Return the result (with any extra trailing space removed if using a list)."""
        output=[]
        s=s.rstrip()
        i=len(s)-1
        while (i>=0):
            if s[i]==' ':
                i -=1
                continue
            j=i
            while (j>=0 and s[j]!=' '):
                j -=1
            output.append(s[j+1:i+1])
            i=j-1
        return  ' '.join(output)