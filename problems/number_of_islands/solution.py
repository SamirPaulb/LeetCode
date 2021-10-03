class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Island = 0
        q = []
        
        def dfs(i, j):
            while q:
                a = q.pop()
                i, j = a[0], a[1]
                if i+1 < len(grid) and grid[i+1][j] == '1':    # Down
                    q.append([i+1, j])
                    grid[i+1][j] = "0"
                if i-1 >= 0 and grid[i-1][j] == '1':           # Up
                    q.append([i-1, j])
                    grid[i-1][j] = "0"
                if j+1 < len(grid[0]) and grid[i][j+1] == '1': # Right
                    q.append([i, j+1])
                    grid[i][j+1] = "0"
                if j-1 >= 0 and grid[i][j-1] == '1':           # Left
                    q.append([i, j-1])
                    grid[i][j-1] = "0"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': 
                    Island += 1
                    grid[i][j] = "0"
                    q.append([i, j])
                    dfs(i, j)

        return Island



