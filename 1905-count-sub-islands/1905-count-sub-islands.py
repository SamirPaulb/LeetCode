class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROW = len(grid1); COL = len(grid1[0])
        def dfs(i, j):
            if not 0<=i<ROW or not 0<=j<COL or grid2[i][j] == 0: return True
            if grid1[i][j] == 0: return False
            ans = True
            grid2[i][j] = grid1[i][j] = 0
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                r = i+dx; c = j+dy
                ans = ans & dfs(r,c)
            return ans
        self.res = 0
        for i in range(ROW):
            for j in range(COL):
                if grid2[i][j] == 1 and dfs(i,j):
                    self.res += 1
        
        return self.res