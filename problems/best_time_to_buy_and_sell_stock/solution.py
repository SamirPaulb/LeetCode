class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I can do only one transaction in this question
        
        minsofar = prices[0]
        maxprofit = 0
        
        for i in range(len(prices)):
            minsofar = min(minsofar, prices[i])
            maxprofit = max(maxprofit, prices[i] - minsofar)
            
            
            
        return maxprofit