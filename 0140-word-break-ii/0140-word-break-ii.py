class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n+1)]
        for i in range(1, n+1):
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    dp[i].append(word)
        
        res = []
        if not dp[-1]: return res
        # print(dp)
        def solve(i, path):
            if i <= 0: 
                res.append(path)
                return
            for st in dp[i]:
                if not path:
                    solve(i-len(st), st)
                else:
                    solve(i-len(st), st + " " + path)
        
        solve(n, "")
        return res