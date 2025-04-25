class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()

        for ch_s, ch_t in zip(s, t):
            if ch_s in mapping:
                if mapping[ch_s] != ch_t:
                    return False
            else:
                if ch_t in mapped:
                    return False
                mapping[ch_s] = ch_t
                mapped.add(ch_t)

        return True
