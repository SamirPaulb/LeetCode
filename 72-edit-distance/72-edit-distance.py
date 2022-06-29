class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        self.res = 0
        dp = [[-1]*(n2+1) for i in range(n1+1)]
        
        def solve(i, j):
            if i == j == 0: return 0
            if i <= 0 or j <= 0: return j or i
            if dp[i][j] != -1: return dp[i][j]
            if word1[i-1] == word2[j-1]:
                ans = solve(i-1, j-1)
            else:
                ans = 1 + min(solve(i, j-1), solve(i-1, j-1), solve(i-1, j))

            dp[i][j] = ans
            return ans
        
        return solve(n1, n2)