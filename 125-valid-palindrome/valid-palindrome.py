class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_text = ''.join(char.lower() for char in s if char.isalnum())
        p1,p2=0,len(clean_text)-1
        while (p1<p2):
            if (clean_text[p1]!=clean_text[p2]):
                return False
            p1 +=1
            p2 -=1
        return True