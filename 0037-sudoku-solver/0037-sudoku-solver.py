class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = {i:set() for i in range(9)}
        col = {i:set() for i in range(9)}
        sub_block = {}
        for i in range(9):
            for j in range(9):
                rs, cs = i//3, j//3
                if (rs,cs) not in sub_block: sub_block[(rs,cs)] = set()
                if board[i][j] != '.':
                    sub_block[(rs,cs)].add(board[i][j])
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
        
        def solve(r,c):
            if r >= len(board): return True
            if c == len(board[0]): return solve(r+1, 0)
            if board[r][c] != '.': return solve(r, c+1) 
            else:
                for i in range(1, 10):
                    s = str(i)
                    if s in row[r] or s in col[c] or s in sub_block[(r//3,c//3)]:
                        continue
                    board[r][c] = s
                    sub_block[(r//3,c//3)].add(s)
                    row[r].add(s)
                    col[c].add(s)
                    if solve(r, c+1): return True
                    board[r][c] = '.'
                    sub_block[(r//3,c//3)].remove(s)
                    row[r].remove(s)
                    col[c].remove(s)
                return False
        
        solve(0, 0)
        return board