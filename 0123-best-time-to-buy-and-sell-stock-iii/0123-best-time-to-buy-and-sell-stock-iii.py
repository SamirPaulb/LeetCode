class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_left = [0]*len(prices)
        minsofar = prices[0]
        maxprofit = 0
        for i, p in enumerate(prices):
            maxprofit = max(maxprofit, p - minsofar)
            minsofar = min(minsofar, p)
            profit_left[i] = maxprofit
        
        profit_right = [0]*len(prices)
        maxsofar = prices[-1]
        maxprofit = 0
        for i in range(len(prices)-1, -1, -1):
            p = prices[i]
            maxprofit = max(maxprofit, maxsofar - p)
            maxsofar = max(maxsofar, p)
            profit_right[i] = maxprofit
        
        res = 0
        for pl, pr in zip(profit_left, profit_right):
            res = max(res, pl+pr)
        # print(profit_left)
        # print(profit_right)
        return res