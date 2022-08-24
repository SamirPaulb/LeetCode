class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(s):
            if s and s[0] == "0": return 0
            if not s or len(s) == 1: return 1
            
            if s in memo: return memo[s]
            
            if int(s[:2]) <= 26: ans = dfs(s[1:]) + dfs(s[2:])
            else: ans = dfs(s[1:])
            
            memo[s] = ans
            return memo[s]
        
        return dfs(s)
            