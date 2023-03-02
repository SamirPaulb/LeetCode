class Solution:
    def minDistance(self, x: str, y: str) -> int:
        dp = [[0]*(len(y)+1) for _ in range(len(x)+1)]
        for i in range(1, len(x)+1):
            for j in range(1, len(y)+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        lcs = dp[-1][-1]
        return len(x) + len(y) - 2 * lcs