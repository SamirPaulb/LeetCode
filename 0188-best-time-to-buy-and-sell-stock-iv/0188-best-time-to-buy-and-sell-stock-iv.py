class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(n) for _ in range(k+1)]
        
        for t in range(1, k+1):
            prevMax = -2**31
            for d in range(1, n):
                prevMax =  max(prevMax, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(dp[t][d-1], prevMax + prices[d])
        # print(dp)
        return dp[-1][-1]