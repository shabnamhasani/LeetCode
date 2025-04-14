class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        if (len(s)%k!=0):
           s +=(k-len(s)%k)*fill

        output=[]
        for i in range(0,len(s),k):
            output.append(s[i:i+k])
        return output


        