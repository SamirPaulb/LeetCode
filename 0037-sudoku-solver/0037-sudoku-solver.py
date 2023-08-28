class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = {i:set() for i in range(10)}
        col = {i:set() for i in range(10)}
        sub = {}
        
        for i in range(9):
            for j in range(9):
                r,c = i//3, j//3
                if (r,c) not in sub:
                    sub[(r,c)] = set()
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sub[(r,c)].add(board[i][j])
        
        def dfs(i, j):
            if j >= 9:
                i += 1
                j = 0
            if i >= 9: return True
            if board[i][j] != '.':
                return dfs(i, j+1)
            for k in range(1, 10):
                v = str(k)
                if v not in row[i] and v not in col[j] and v not in sub[(i//3,j//3)]:
                    row[i].add(v)
                    col[j].add(v)
                    sub[(i//3,j//3)].add(v)
                    board[i][j] = v
                    if dfs(i, j+1): return True
                    row[i].remove(v)
                    col[j].remove(v)
                    sub[(i//3,j//3)].remove(v)
                    board[i][j] = '.'
            return False
        
        dfs(0, 0)
        return board
