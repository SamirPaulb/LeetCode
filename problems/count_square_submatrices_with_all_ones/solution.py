class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for i in range(1,len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                count += matrix[i][j]
        count += sum(matrix[0])
        for i in range(1, len(matrix)):
            count += matrix[i][0]
        return count