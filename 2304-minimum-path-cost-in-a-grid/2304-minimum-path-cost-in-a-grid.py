class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = self.deepcopy(grid)
        
        for i in range(1, row):
            for j in range(col):
                val = 2**31
                for k in range(col):
                    val = min(val, dp[i-1][k] + moveCost[grid[i-1][k]][j])
                dp[i][j] += val
        
        return min(dp[-1])
    
    
    def deepcopy(self, arr):
        n = len(arr)
        m = len(arr[0])
        new_arr = [[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                new_arr[i][j] = arr[i][j]
        
        return new_arr