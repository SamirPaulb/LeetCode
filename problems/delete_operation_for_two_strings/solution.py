class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x = word1; y = word2; m = len(x); n = len(y)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        lcs = dp[-1][-1]
        
        d = m - lcs
        i = n - lcs
        
        return d + i