# https://www.youtube.com/watch?v=BzTIOsC0xWM
# Traversing from bottom-right most to top-left most corner
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid); c = len(grid[0])
        
        # in (c-1)th coloumn only 1 path available. ie, straight down. So bottom to up path along right most column is continuous sum of elements
        for i in range(r-2, -1, -1):
            grid[i][c-1] += grid[i+1][c-1]
        
        # in (r-1)th row only 1 path is available => straight right. so right to left path along bottom most row is contigeuos sum of elements
        for j in range(c-2, -1, -1):
            grid[r-1][j] += grid[r-1][j+1]
        
        # from (r-2, c-2) to (0, 0) path => in any cell add minimum value of down or right cell 
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]
    