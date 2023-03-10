class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
        dp = {}
        def dfs(i, j, k):
            if k == 0: return 1
            if (i,j,k) in dp: return dp[(i,j,k)]
            prob = 0
            for dx, dy in moves:
                r, c = i+dx, j+dy
                if 0<=r<n and 0<=c<n:
                    prob += dfs(r, c, k-1)
            dp[(i,j,k)] = prob/8
            return prob/8
        
        return dfs(row, column, k)