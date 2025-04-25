from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        for ch in ransomNote:
            if magazine_counter[ch] <= 0:  # <- fix here
                return False
            magazine_counter[ch] -= 1
        return True