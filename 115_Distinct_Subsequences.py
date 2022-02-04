class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/51131/space-o-mn-and-o-n-python-solutions
        dp = [[0 for j in xrange(0, len(t) + 1)] for i in xrange(0, len(s) + 1)]
        for j in xrange(1, len(t) + 1):
            dp[0][j] = 0
        for i in xrange(1, len(s) + 1):
            dp[i][0] = 1
        dp[0][0] = 1
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])

        return dp[-1][-1]
