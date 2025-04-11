class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])  # m = rows, n = columns
        for i in range(n):
            val=grid[0][i]
            for j in range (m-1):
                if grid[j][i] != grid[j+1][i]:
                    return False
        for i in range(n-1):
            val=grid[0][i]
            if val ==grid[0][i+1]:
                return False
        return True

        