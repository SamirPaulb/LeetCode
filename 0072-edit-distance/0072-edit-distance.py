class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[-1]*(len(w2)+1) for i in range(len(w1)+1)]
        
        def solve(i, j):
            if i == 0 or j == 0: return j or i
            if dp[i][j] != -1: return dp[i][j]
            ans = 0
            if w1[i-1] == w2[j-1]:
                ans = solve(i-1, j-1)
            else:
                ans = 1 + min(solve(i-1, j-1), solve(i-1, j), solve(i, j-1))
            dp[i][j] = ans
            return ans
        
        return solve(len(w1), len(w2))
    