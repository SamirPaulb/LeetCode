class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[""] for _ in range(n+1)]
        for i in range(1, n+1):
            arr = []
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    if i-len(word) == 0:
                        arr.append(word)
                    elif dp[i-len(word)] != [""]:
                        for st in dp[i-len(word)]:
                            arr.append(st + " " + word)
            dp[i] = arr
            
        # print(dp)
        return dp[-1]