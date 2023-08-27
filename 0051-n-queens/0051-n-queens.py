class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        col = set()
        pos = set()
        neg = set()
        res = []
        def solve(r):
            if r >= n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c not in col and r+c not in pos and r-c not in neg:
                    col.add(c)
                    pos.add(r+c)
                    neg.add(r-c)
                    board[r][c] = 'Q'
                    solve(r+1)
                    col.remove(c)
                    pos.remove(r+c)
                    neg.remove(r-c)
                    board[r][c] = '.'
        
        solve(0)
        return res
