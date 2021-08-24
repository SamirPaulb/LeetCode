class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int: 
    	M, N, p = len(grid), len(grid[0]), 0
    	for m in range(M):
    		for n in range(N):
    			if grid[m][n] == 1:
    				if m == 0   or grid[m-1][n] == 0: p += 1
    				if n == 0   or grid[m][n-1] == 0: p += 1
    				if n == N-1 or grid[m][n+1] == 0: p += 1
    				if m == M-1 or grid[m+1][n] == 0: p += 1
    	return p
		