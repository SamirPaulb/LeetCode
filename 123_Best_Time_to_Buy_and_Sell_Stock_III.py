class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     # https://discuss.leetcode.com/topic/4766/a-clean-dp-solution-which-generalizes-to-k-transactions
    #     ls = len(prices)
    #     if ls == 0:
    #         return 0
    #     num_t, max_profit = 2, 0
    #     dp = [[0] * ls for _ in range(num_t + 1)]
    #     for t in range(1, num_t + 1):
    #         tempMax = dp[t - 1][0] - prices[0]
    #         for i in range(1, ls):
    #             dp[t][i] = max(dp[t][i - 1], prices[i] + tempMax)
    #             tempMax = max(tempMax, dp[t - 1][i] - prices[i])
    #             max_profit = max(dp[t][i], max_profit)
    #     return max_profit

    # https://discuss.leetcode.com/topic/50360/python-dp-and-non-dp-solution
    def maxProfit(self, prices):
        ls = len(prices)
        if ls == 0:
            return 0
        b1 = b2 = -prices[0]
        s1 = s2 = 0
        for i in xrange(1, ls):
            s2 = max(s2, b2 + prices[i])
            b2 = max(b2, s1 - prices[i])
            s1 = max(b1 + prices[i], s1)
            b1 = max(b1, -prices[i])
        return max(s1, s2)

