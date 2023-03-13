class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n)]
        # dp = {i : [] for i in range(len(s))}
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i].append(word)
        
        res = []
        if not dp[0]: return res
        
        def solve(i, path):
            if i >= len(s): 
                res.append(path)
                return
            for st in dp[i]:
                if not path:
                    solve(i+len(st), st)
                else:
                    solve(i+len(st), path + " " + st)
        
        solve(0, "")
        return res