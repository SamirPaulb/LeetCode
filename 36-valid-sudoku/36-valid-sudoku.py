class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDic = {i:set() for i in range(9)}
        colDic = {i:set() for i in range(9)}
        subboxesDic = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                # check for row
                if board[i][j] in rowDic[i]: return False
                else: rowDic[i].add(board[i][j])
                
                # check for column
                if board[i][j] in colDic[j]: return False
                else: colDic[j].add(board[i][j])
                
                # check for sub-boxes
                key = str(i//3) + str(j//3)
                if key not in subboxesDic: subboxesDic[key] = {board[i][j]}
                else:
                    if board[i][j] in subboxesDic[key]: return False
                    else: subboxesDic[key].add(board[i][j])
        
        return True