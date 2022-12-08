class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = {i:0 for i in set(p)}
        tmp = 0
        for i in range(len(p)):
            if (ord(p[i-1]) - 96) % 26 == (ord(p[i]) - 97):
                tmp += 1
            else:
                tmp = 1
            dp[p[i]] = max(dp[p[i]], tmp)
        # print(dp)
        return sum(dp.values())