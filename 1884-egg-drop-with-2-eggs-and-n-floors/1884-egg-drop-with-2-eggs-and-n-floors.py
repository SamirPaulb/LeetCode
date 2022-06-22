class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[-1]*4 for f in range(n+2)]
        
        def solve(e, f):
            if f == 0 or f == 1: return f
            if e == 1: return f
            if dp[f][e] != -1:
                return dp[f][e]
            ans = 2**31
            for k in range(1, f+1):
                tmp = 1 + max(solve(e-1, k-1), solve(e, f-k))
                ans = min(ans, tmp)
            dp[f][e] = ans
            return dp[f][e]
        
        return solve(2, n)