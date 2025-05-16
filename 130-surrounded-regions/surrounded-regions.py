"""
Step 1: Iterate over the border (first/last row and first/last column)
For each 'O' on the border, mark all connected 'O's (using DFS/BFS) — e.g., change them to '#' temporarily.
Step 2: Go through the full board:
Convert remaining 'O's to 'X' (these are truly surrounded).
Convert '#'s back to 'O' (these were connected to the border)."""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = '#'
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
