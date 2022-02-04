class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # bottom up o(m*n)
        # https://leetcode.com/discuss/93024/easy-dp-java-solution-with-detailed-explanation
        if s == p:
            return True
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n):
            if p[j] == '*' and dp[0][j - 1]:
                dp[0][j + 1] = True
        # print dp
        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isMatch("", ".*")


