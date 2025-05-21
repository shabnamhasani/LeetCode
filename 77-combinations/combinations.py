"""You need to explore all subsets of size k from numbers 1 to n. This is a classic backtracking problem."""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result
