class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
        res = -1
        while q:
            res += 1
            n = len(q)
            for _ in range(n):
                i,j = q.popleft()
                for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                    r,c = i+x,j+y
                    if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 0:
                        grid[r][c] = 1
                        q.append((r,c))
        return res if res != 0 else -1