import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INT_MAX = sys.maxsize
        dp = [[INT_MAX]*(amount+1) for i in range(len(coins)+1)]
                
        for i in range(len(coins)+1):
            dp[i][0] = 0
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1+ dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                    
        
        return dp[-1][-1] if dp[-1][-1] != INT_MAX else -1
            