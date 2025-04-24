class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

        for _ in range(4):  # 0, 90, 180, 270
            if mat == target:
                return True
            mat = rotate(mat)
        return False
