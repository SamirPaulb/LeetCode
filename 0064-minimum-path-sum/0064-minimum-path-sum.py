class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid); col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if i == j == 0: continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        print(grid)
        return grid[-1][-1]