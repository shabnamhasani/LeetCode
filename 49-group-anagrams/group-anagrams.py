from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map= defaultdict(list)
        for word in strs:
           key=''.join(sorted(word))
           anagrams_map[key].append(word)
        return list(anagrams_map.values())