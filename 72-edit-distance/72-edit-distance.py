'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if i == 0 or j == 0: return j or i
                        
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i-1] == word2[j-1]:
                ans = dfs(i-1, j-1)
            else: 
                ans = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
                
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return dfs(len(word1), len(word2))
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0: dp[i][j] = j
                elif j == 0: dp[i][j] = i
                elif word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]