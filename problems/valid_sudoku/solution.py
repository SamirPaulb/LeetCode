class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                
                # checking the coloums
                for k in range(n):
                    if board[i][j] == board[i][k] and k != j:
                        return False
                
                #checking the rows
                for k in range(n):
                    if board[i][j] ==  board[k][j] and i != k:
                        return False
                
                #checking the grid
                xi = (i//3)*3 #rows of single grid
                yj = (j//3)*3 #coloums of single grid
                for r in range(xi, xi+3):
                    for c in range(yj, yj+3):
                        if board[r][c] == board[i][j] and i != r and j != c:
                            return False
        return True
    