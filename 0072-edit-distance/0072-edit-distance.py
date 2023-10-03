class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n1, n2 = len(w1), len(w2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i
        
        for j in range(n2+1):
            dp[0][j] = j
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[-1][-1]
