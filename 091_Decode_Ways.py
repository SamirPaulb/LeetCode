class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        if ls == 0:
            return 0
        dp = [0] * ls
        for index in range(ls):
            if index >= 1 and int(s[index - 1:index + 1]) < 27 and int(s[index - 1:index + 1]) >= 10:
                if index == 1:
                    dp[index] = 1
                else:
                    # 11-26
                    dp[index] += dp[index - 2]
            if int(s[index]) != 0:
                if index == 0:
                    dp[index] = 1
                else:
                    # 1-9
                    dp[index] += dp[index - 1]
        return dp[ls - 1]
