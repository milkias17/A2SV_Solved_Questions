class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(matrix):
            for j in range(i + 1, len(row)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i, row in enumerate(matrix):
            for j in range(len(row) // 2):
                other = len(row) - 1 - j
                matrix[i][j], matrix[i][other] = matrix[i][other], matrix[i][j]
