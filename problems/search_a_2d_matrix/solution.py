class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[i])-1]:
                row = i
                break
        if row == -1: return False
        for i in range(len(matrix[row])):
            if matrix[row][i] == target:
                return True
        return False
            