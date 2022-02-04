class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        max_profit, low = 0, prices[0]
        for i in range(1, length):
            if low > prices[i]:
                low = prices[i]
            else:
                temp = prices[i] - low
                if temp > max_profit:
                    max_profit = temp
        return max_profit