class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp = [1, 10]
        for i in range(2, n+1):
            tmp = 81
            for j in range(1, i-1):
                tmp *= (9 - j)
            ans = dp[i-1] + tmp
            dp.append(ans)
        
        return dp[n]
                