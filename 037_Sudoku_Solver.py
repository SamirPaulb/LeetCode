class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #https://leetcode.com/discuss/84831/java-backtracking-stack-20ms
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append(9 * i + j)
        self.solve(board, empty)

    def solve(self, board, empty):
        if len(empty) == 0:
            return True
        first_value = empty[-1]
        row, col = first_value / 9, first_value % 9
        for k in range(1, 10):
            if self.is_safe(board, row, col, str(k)):
                board[row][col] = str(k)
                empty.pop()
                if self.solve(board, empty):
                    return True
                board[row][col] = '.'
                empty.append(first_value)
        return False

    def is_safe(self, board, row, col, ch):
        for k in range(9):
            if board[k][col] == ch:
                return False
            if board[row][k] == ch:
                return False
        start_row, start_col = 3 * (row / 3), 3 * (col / 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == ch:
                    return False
        return True


