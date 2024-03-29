class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        x = str1; y = str2; m = len(x); n = len(y)
        dp = [[0]*(n+1) for  i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        res = ""
        i = m ; j = n
        while i > 0 and j > 0:
            if x[i-1] == y[j-1]:
                res += x[i-1]
                i -= 1; j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    res += x[i-1]
                    i -= 1
                else:
                    res += y[j-1]
                    j -= 1
        while i > 0:
            res += x[i-1]; i -= 1
        while j > 0: res += y[j-1]; j -= 1
        return res[::-1]