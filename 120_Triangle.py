class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0:
            return 0
        ls = len(triangle)
        dp = [0] * ls
        dp[0] = triangle[0][0]
        for i in range(1, ls):
            # note that dp should be updated in reversed order
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in reversed(range(1, i)):
                dp[j] = min(dp[j - 1] + triangle[i][j], dp[j] + triangle[i][j])
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)
