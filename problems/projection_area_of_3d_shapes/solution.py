class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        s = 0
        for i in range(len(grid)):
            x_max = max(grid[i])
            y_max = 0
            for j in range(len(grid)):
                if grid[j][i] > y_max: y_max = grid[j][i]
                if grid[i][j]: s += 1
                    
            s += x_max + y_max
        
        return s