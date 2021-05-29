class Solution:
    def totalNQueens(self, N: int) -> int:
        self.ans = 0

        def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
            if i == N: self.ans += 1
            else:
                for j in range(N):
                    vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (N-i-1+j)
                    if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                    place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)

        place(0,0,0,0)
        return self.ans
