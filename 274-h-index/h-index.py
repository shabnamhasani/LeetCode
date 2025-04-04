class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """[3,0,6,1,5]> [6,5,3,1,0]"""
        citations.sort(reverse=True)
        h_index=0
        for i, c in enumerate(citations):
            if c >=i+1:
                h_index=i+1
            else:
                break 
        return h_index
        