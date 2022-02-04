class Solution(object):
    # def numWays(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     w = [0, k, k*k]
    #     while len(w) <= n:
    #         w += sum(w[-2:]) * (k-1),
    #     return w[n]
    def numWays(self, n, k):
        if n == 0:
            return 0
        elif n == 1:
            return k
        # two step dp
        # ways[1] = k
        # ways[2] = k * k
        # ways[i>2] = (ways[i-1] + ways[i-2]) * (k - 1)
        dp = [0] * 2
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            temp = dp[1]
            dp[1] = sum(dp) * (k - 1)
            dp[0] = temp
        return dp[1]