class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        
        for j in range(amount+1):
            dp[0][j] = float('inf')
        
        for j in range(1, amount+1):
            if j%coins[0]==0:
                dp[1][j] = j//coins[0]
            else:
                dp[1][j] = float('inf')
        
        for i in range(2, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1 + dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        ans = dp[-1][-1]
        return ans if ans != float('inf') else -1