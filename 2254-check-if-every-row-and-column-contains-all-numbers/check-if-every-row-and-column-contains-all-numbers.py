class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        required = set(range(1,n+1))
        for i in range(n):
            # Check the i-th row
            if(set(matrix[i])!=required):
                return False
            # Check the i-th col
            col={matrix[j][i] for j in range(n)}
            if col!=required:
                return False
    
        return True