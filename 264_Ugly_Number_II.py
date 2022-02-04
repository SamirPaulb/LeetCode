class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        dp = [0] * (n + 1)
        l1 = l2 = l3 = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        dp[5] = 5
        for i in range(6, n + 1):
            while dp[l1] * 2 <= dp[i - 1]:
                l1 += 1
            while dp[l2] * 3 <= dp[i - 1]:
                l2 += 1
            while dp[l3] * 5 <= dp[i - 1]:
                l3 += 1
            print l1, l2, l3
            dp[i] = min(dp[l1] * 2, dp[l2] * 3, dp[l3] * 5)
        # print dp
        return dp[n]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.nthUglyNumber(10)