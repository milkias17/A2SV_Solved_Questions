from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = [[None for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                new_matrix[j][i] = col

        return new_matrix
