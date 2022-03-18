class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row,column = len(matrix),len(matrix[0])
        res = 0
        
        dp = [[0 for _ in range(column)] for _ in range(row)]
        for i in range(row):
            for j in range(column):
                if i==0 or j==0:
                    dp[i][j]= int(matrix[i][j])-0;  
                else: 
                    if matrix[i][j] == '1':
                        dp[i][j] = int(min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])) + 1
                res = max(res,dp[i][j])
                
        return pow(res,2)
                
