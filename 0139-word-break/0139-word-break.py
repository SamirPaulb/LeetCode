class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(l, r):
            if l >= len(s): return True
            if r >= len(s): return False
            if (l,r) in dp: return dp[(l,r)]
            cur = s[l:r+1]
            if cur in wordDict:
                ans = dfs(r+1, r+1) or dfs(l, r+1)
            else:
                ans = dfs(l, r+1)
            dp[(l,r)] = ans
            return ans
        
        return dfs(0, 0)