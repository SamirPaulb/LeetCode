class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for i in range(len(coins)+1)] 
        for i in range(1, len(coins)+1):
            for j in range(0, amount+1):
                if j == 0:
                    dp[i][j] = 1
                    
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-coins[i-1]])
                print(dp[i][j], end = " ")
            print()
        return dp[len(coins)][-1]