class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]
        for p in prices[1:]:
            res = max(res, p - mini)
            mini = min(mini, p)
        return res