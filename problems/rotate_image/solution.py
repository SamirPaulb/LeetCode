class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            a = 0
            b = n-1
            while a< b:
                matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
                a += 1
                b -= 1
                
                
                
        
                
                
        