class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid (board) and self.is_col_valid(board) and self.is_box_valid(board))
    def is_row_valid(self, board) -> bool:
        rows = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)
        return True
    def is_col_valid(self, board) -> bool:
        cols = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)
        return True
    def is_box_valid(self, board) -> bool:
        boxes =[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                # Check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        return True