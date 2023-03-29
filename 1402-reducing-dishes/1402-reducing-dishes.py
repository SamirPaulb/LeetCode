class Solution:
    def maxSatisfaction(self, sati: List[int]) -> int:
        sati.sort()
        dp = {}
        # [-9, -8, -1, 0, 5]
        def dfs(i, j):
            if i >= len(sati): return 0
            if (i,j) in dp: return dp[(i,j)]
            ans = max(dfs(i+1, j), j * sati[i] + dfs(i+1, j+1))
            dp[(i,j)] = ans
            return ans
        
        return dfs(0, 1)