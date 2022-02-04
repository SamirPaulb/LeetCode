class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # recusive
        if n == 0:
            return 0
        res = []
        board = [['.'] * n for t in range(n)]
        self.do_solveNQueens(res, board, n)
        return res

    def do_solveNQueens(self, res, board, num):
        if num == 0:
            res.append([''.join(t) for t in board])
            return
        ls = len(board)
        pos = ls - num
        check = [True] * ls
        for i in range(pos):
            for j in range(ls):
                if board[i][j] == 'Q':
                    check[j] = False
                    step = pos - i
                    if j + step < ls:
                        check[j + step] = False
                    if j - step >= 0:
                        check[j - step] = False
                    break
        for j in range(ls):
            if check[j]:
                board[pos][j] = 'Q'
                self.do_solveNQueens(res, board, num - 1)
                board[pos][j] = '.'


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.solveNQueens(4)