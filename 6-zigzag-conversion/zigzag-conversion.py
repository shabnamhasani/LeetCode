class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """Flip direction when you hit the top or bottom.
        Update current row based on direction."""
        if numRows==1 or numRows >= s:
            return s

        down= False
        rows = [""] * numRows
        current_row=0
        for i in range(len(s)):
            rows[current_row]+=(s[i]) #rows is a list of strings, not lists of characters, so you should concatenate using +=
            if (current_row==0 or current_row==numRows-1):
                down= not down

            if (down):
                current_row +=1
            else:
                current_row -=1

        return "".join(rows)