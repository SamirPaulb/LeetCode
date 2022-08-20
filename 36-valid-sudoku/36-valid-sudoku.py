class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i:set() for i in range(9)}
        col = {j:set() for j in range(9)}
        sub_box = {(i, j):set() for j in range(3) for i in range(3)}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                num = board[i][j] 
                if num in row[i]: return False
                row[i].add(num)
                if num in col[j]: return False
                col[j].add(num)
                key = (i//3, j//3)
                if num in sub_box[key]: return False
                sub_box[key].add(num)
        
        return True