class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            for x, y in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(i+x, j+y)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
                
        return res