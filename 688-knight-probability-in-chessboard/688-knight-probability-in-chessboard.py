class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,-2],[1,2],[-1,-2],[-1,2]]  # all possible moves of knight in 8 directions.
        
        memo =  {}   # to store answer of each calls
        
        def dfs(r, c, k):
            if (not 0 <= r < n) or (not 0 <= c < n):  # We're already outside the grid, so probability of staying inside is 0
                return 0  
            if k == 0:   # We're inside the grid and have no more moves to make
                return 1  
            
            key = (r, c, k)
            if key in memo:   # previously this call was made and calculated answer of this call is stored in memo
                return memo[key]
            
            tmp = 0
            for m in move:  # we make 8 possible moves and find the probability of staying inside after k - 1 more moves.
                tmp += dfs(r+m[0], c+m[1], k-1)
            
            memo[key] = tmp / 8   # as each move is equally likely, we average all of these probabilities.
            return memo[key]      # update memo to memozition to use this in future calls to avoid same calculation again.
        
        return dfs(row, column, k)
