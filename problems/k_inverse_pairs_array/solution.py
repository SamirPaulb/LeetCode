class Solution:
    def kInversePairs(self, n: int, k: int) -> int: 
        dp = [[0] * (k+1) for i in range(n+1)]
        dp[0][0] = 1
            
        for i in range(1, n+1):
            for j in range(k+1):
                dp[i][j] += sum(dp[i-1][max(0, j-i+1): j+1])
                dp[i][j] = dp[i][j] % (10 ** 9 + 7)

        return dp[n][k]