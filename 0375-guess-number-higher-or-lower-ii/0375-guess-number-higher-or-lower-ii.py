class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[2**31]*(n+1) for _ in range(n+1)]
        
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                if i == j:
                    dp[i][j] = 0
                if j - i == 1: 
                    dp[i][j] = i
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        # print(dp)
        return dp[1][-1]