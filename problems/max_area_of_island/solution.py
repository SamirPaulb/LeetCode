class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        def trav(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
        for i, j in product(range(n), range(m)):
            if grid[i][j]: ans = max(ans, trav(i, j))
        return ans
