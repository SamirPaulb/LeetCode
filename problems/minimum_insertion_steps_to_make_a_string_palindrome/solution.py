class Solution:
    def minInsertions(self, s: str) -> int:
        # Minimum Number of insertions = len(S) - LCS
        def LCS(X, Y):
            m = len(X); n = len(Y)
            dp = [[0]*(len(Y)+1) for i in range(len(X)+1)]
            for i in range(1, len(X)+1):
                for j in range(1, len(Y)+1):
                    if X[i-1] == Y[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[-1][-1]
        
        return len(s) - LCS(s, s[::-1])
    