class Solution(object):
    # def getMoneyAmount(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     #top down dp
    #     dp = [[0] * (n + 1) for _ in range(n + 1)]
    #     return self.top_down_dp(dp, 1, n)
    #
    # def top_down_dp(self, dp, begin, end):
    #     if begin >= end:
    #         return 0
    #     if dp[begin][end] != 0:
    #         return dp[begin][end]
    #     res = sys.maxint
    #     for i in xrange(begin, end + 1):
    #         tmp = i + max(self.top_down_dp(dp, begin, i - 1), self.top_down_dp(dp, i + 1, end))
    #         res = min(res, tmp)
    #     dp[begin][end] = res
    #     return res

    def getMoneyAmount(self, n):
        # bottom up dp
        # https://discuss.leetcode.com/topic/51353/simple-dp-solution-with-explanation/2
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(2, n + 1):
            for i in range(j - 1, 0, -1):
                globalMin = sys.maxint
                for k in range(i + 1, j):
                    localMax = k + max(dp[i][k - 1], dp[k + 1][j])
                    globalMin = min(globalMin, localMax)
                if i + 1 == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = globalMin
        return dp[1][n]
