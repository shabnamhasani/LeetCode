class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """We only want to swap elements above the main diagonal, because the rest will be covered when i and j flip."""
        n = len(matrix)
        
        # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range (i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

        