class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        countOfFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    countOfFresh += 1
                    
        if countOfFresh == 0: return 0                                       
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        res = 0
        while q:
            res += 1
            n = len(q)
            for i in range(n):
                r, c = q.pop(0)
                for m in move:
                    nr = r + m[0]
                    nc = c + m[1]
                    
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        
        countOfFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    countOfFresh += 1
                    
        if countOfFresh == 0: return res-1
        return -1