class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        for j in range(1, c):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        
        for i in range(1, r):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
    