class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid2), len(grid2[0])
        def dfs(i,j):
            if not 0<=i<row or not 0<=j<col or grid2[i][j] == 0: return 
            grid2[i][j] = 0
            for x,y in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(i+x,j+y)
        
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:
                    if grid1[i][j] == 0:
                        dfs(i,j)
        res = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    res += 1
        return res