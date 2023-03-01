class Solution:
    def numSquares(self, n: int) -> int:
        sqn = int(math.sqrt(n))
        dp = [[2**31]*(n+1) for _ in range(sqn+1)]
        for i in range(sqn+1):
            dp[i][0] = 0
        for i in range(1, sqn+1):
            for j in range(1, n+1):
                sq = i*i
                if sq <= j:
                    dp[i][j] = min(1 + dp[i][j-sq], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]