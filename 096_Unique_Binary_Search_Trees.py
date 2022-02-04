class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/discuss/86650/fantastic-clean-java-dp-solution-with-detail-explaination
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for level in range(2, n + 1):
            for root in range(1, level + 1):
                dp[level] += dp[level - root] * dp[root - 1]
        return dp[n]