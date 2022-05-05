'''
use dummy arrays to check if the particular row or column has an element 0 or not
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [-1] * len(matrix)
        col = [-1] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        
        for i in range(len(matrix)):
            if row[i] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if col[j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        return matrix
# Time: O(N * M)
# Space: O(N + M)
