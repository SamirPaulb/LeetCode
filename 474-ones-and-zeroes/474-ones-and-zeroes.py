class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for s in strs:
            z = s.count('0')
            o = len(s) - z
            for i in range(m, z-1, -1):
                for j in range(n, o-1, -1):
                    dp[i][j] = max(1 + dp[i-z][j-o], dp[i][j])
        
        return dp[m][n]
    

# Time: O(len(strs) * m * n)
# Space: O(m * n)