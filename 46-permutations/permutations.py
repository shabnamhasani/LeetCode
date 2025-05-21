"""We generate permutations by trying each number at each position and backtracking once we've gone down one path."""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return res
