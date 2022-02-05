class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                tmp = 0
                q = [(i,j)]
                while q:
                    a = q.pop()
                    i = a[0]; j = a[1]
                    if grid[i][j] == 0: continue
                    tmp += 1
                    grid[i][j] = 0
                    if i>0 and grid[i-1][j] == 1: q.append([i-1, j])
                    if i+1<m and grid[i+1][j] == 1: q.append([i+1, j])
                    if j>0 and grid[i][j-1] == 1: q.append([i, j-1])
                    if j+1<n and grid[i][j+1] == 1: q.append([i, j+1])
                res = max(res, tmp)
        
        return res