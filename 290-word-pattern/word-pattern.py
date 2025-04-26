class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        c_p_s_mapping={}
        c_s_p_mapping={}
        if len(pattern)!=len(words):
            return False
        for c_p, c_s in zip (pattern,words):
            if c_p in c_p_s_mapping:
                if c_p_s_mapping[c_p] !=c_s:
                    return False
            else:
                c_p_s_mapping[c_p]=c_s
            if c_s in c_s_p_mapping:
                if c_s_p_mapping[c_s] !=c_p:
                    return False
            else:
                c_s_p_mapping[c_s]=c_p
        return True