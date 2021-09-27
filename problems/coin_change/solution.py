class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf")]*(amount+1) for i in range(len(coins)+1)]
        
        for i in range(1, len(coins)+1):
            for j in range(0, amount + 1):
                if j == 0:
                    dp[i][j] = 0
                    
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                
                else:
                    dp[i][j] = min(dp[i-1][j], 1+ dp[i][j - coins[i-1]])
        
        if dp[-1][-1] == float("inf"):
            return -1
        return dp[-1][-1]