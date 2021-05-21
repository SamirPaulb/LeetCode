class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        maxprofit = 0
        for  i in range(len(prices)):
            minsofar = min(minsofar , prices[i])
            profit = prices[i] - minsofar 
            maxprofit = max(maxprofit, profit)
        
        return maxprofit
        