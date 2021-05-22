class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        ans = []
        board = [['.'] * N for _ in range(N)]

        def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
            if i == N:
                ans.append(["".join(row) for row in board])
                return
            for j in range(N):
                vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (N-i-1+j)
                if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                board[i][j] = 'Q'
                place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)
                board[i][j] = '.'

        place(0,0,0,0)
        return ans
