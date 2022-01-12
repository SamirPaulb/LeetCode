class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # swap left columns with right  columns
        l = 0; r = n-1
        while l < r:
            for i in range(n):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            
            l += 1
            r -= 1
        
        
        