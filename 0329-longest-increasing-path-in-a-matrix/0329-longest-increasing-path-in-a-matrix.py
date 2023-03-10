class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[-1]*col for _ in range(row)]
        
        def dfs(i, j, prev):
            if not 0 <= i < row or not 0<=j<col or matrix[i][j] == '#': return 0
            if prev >= matrix[i][j]: return 0
            if dp[i][j] != -1: return dp[i][j]
            
            ans = 0
            tmp = matrix[i][j]
            matrix[i][j] = "#"
            for dx, dy in ((1,0), (-1,0), (0,-1), (0,1)):
                r, c = i+dx, j+dy
                ans = max(ans, 1 + dfs(r, c, tmp))
            matrix[i][j] = tmp
            dp[i][j] = ans
            return ans
        
        res = 1
        for i in range(row):
            for j in range(col):
                res = max(res, dfs(i, j, -2**31))
        
        return res