class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}
        def solve(a, b):
            if len(a) != len(b): return False
            if a == b: return True
            if len(a) <= 1 or len(b) <= 1: return False
            if sorted(a) != sorted(b): return False
            key = a + "-" + b
            if key in dp: return dp[key]
            n = len(a)
            for k in range(1, n):
                noswap = solve(a[:k], b[:k]) and solve(a[k:], b[k:])
                swap = solve(a[:k], b[n-k:]) and solve(a[k:], b[:n-k])
                if noswap or swap: 
                    dp[key] = True
                    return True
            dp[key] = False
            return False
        
        return solve(s1, s2)