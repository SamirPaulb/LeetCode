class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        X = text1; Y = text2; m = len(X); n  = len(Y)
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1]
    