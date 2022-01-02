class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        x = s; y =s[::-1]; n = len(x)
        dp = [[0]*(n+1) for  i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        
        return dp[-1][-1]
    