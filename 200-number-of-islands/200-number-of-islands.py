class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        r = len(grid)
        c = len(grid[0])
        
        def makeWater(i, j):
            if (not 0 <= i < r) or (not 0 <= j < c) or grid[i][j] == "0": 
                return
            grid[i][j] = "0"
            makeWater(i+1, j)
            makeWater(i-1, j)
            makeWater(i, j+1)
            makeWater(i, j-1)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    res += 1
                    makeWater(i, j)
        
        return res