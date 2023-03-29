class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        n = len(A)
        A.sort()
        dp = [[-1]*(n+1) for _ in range(n+1)]
        
        def dfs(i, j):
            if i >= len(A): return 0
            if dp[i][j] != -1: return dp[i][j]
            ans = max(dfs(i+1, j), j * A[i] + dfs(i+1, j+1))
            dp[i][j] = ans
            return ans
        
        return dfs(0, 1)