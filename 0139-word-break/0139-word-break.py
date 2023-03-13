class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i+len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i] == True:
                        break
                        
        # print(dp)
        return dp[0]