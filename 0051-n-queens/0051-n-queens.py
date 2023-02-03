class Solution:
    def solveNQueens(self, n):
        col, posDiag, negDiag = set(), set(), set()
        board = [['.']*n for _ in range(n)]
        res = []
        
        def dfs(i):
            if i == n: 
                res.append(["".join(board[i]) for i in range(n)])
                return 
            for j in range(n):
                if j not in col and (i+j) not in posDiag and (i-j) not in negDiag:
                    board[i][j] = 'Q'
                    col.add(j)
                    posDiag.add(i+j)
                    negDiag.add(i-j)
                    
                    dfs(i+1)
                    
                    board[i][j] = '.'
                    col.remove(j)
                    posDiag.remove(i+j)
                    negDiag.remove(i-j)
            
        dfs(0)
        return res