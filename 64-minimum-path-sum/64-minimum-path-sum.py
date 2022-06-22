class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if i == j == 0: continue
                elif i == 0: grid[i][j] += grid[i][j-1]
                elif j == 0: grid[i][j] += grid[i-1][j]
        
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]