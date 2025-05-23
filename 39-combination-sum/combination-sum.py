class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(start, path, remaining):
            print(f"Calling backtrack(start={start}, path={path}, remaining={remaining})")
            if remaining == 0:
                print(f"Found valid path: {path}")
                result.append(path[:])
                return
            if remaining < 0:
                print(f"Overshot target with path: {path}, backtracking...")
                return

            for i in range(start, len(candidates)):
                # Choose candidates[i]
                path.append(candidates[i])
                print(f"Include {candidates[i]}, path now: {path}")
                backtrack(i, path, remaining - candidates[i])  # not i+1, since we can reuse the number
                print(f"Backtrack: remove {path[-1]} from {path}")
                path.pop()

        backtrack(0, [], target)
        return result
