class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = list(s.split(' '))
        if len(s) != len(p): return False
        dp = {}
        ds = {}
        for ep, es in zip(p, s):
            if ep not in dp:
                dp[ep] = es
            else:
                if dp[ep] != es: return False
            
            if es not in ds:
                ds[es] = ep
            else:
                if ds[es] != ep: return False
        
        return True