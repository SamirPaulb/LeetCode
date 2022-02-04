class Solution(object):
    def solve(self, board):
        # https://discuss.leetcode.com/topic/22503/some-tips-for-python-code
        if not board:
            return
        height, width = len(board), len(board[0])
        leakWall = self.buildLeakWall(board)
        while leakWall:
            i, j = leakWall.pop()
            if 0 <= i < height and 0 <= j < width:
                if board[i][j] == "O":
                    board[i][j] = "S"
                    leakWall += (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        for i in range(height):
            for j in range(width):
                board[i][j] = "O" if board[i][j] == "S" else "X"

    def buildLeakWall(self, board):
        leakWall, height, width = [], len(board), len(board[0])
        for i in range(height):
            if board[i][0] == "O":
                leakWall.append((i, 0))
            if board[i][width - 1] == "O":
                leakWall.append((i, width - 1))
        for j in range(width):
            if board[0][j] == "O":
                leakWall.append((0, j))
            if board[height - 1][j] == "O":
                leakWall.append((height - 1, j))
        return leakWall

    # def solve(self, board):
    #     # https://leetcode.com/problems/surrounded-regions/
    #     if not any(board): return
    #
    #     height, width = len(board), len(board[0])
    #     save = [ij for k in range(height + width) for ij in ((0, k), (height - 1, k), (k, 0), (k, width - 1))]
    #     while save:
    #         i, j = save.pop()
    #         if 0 <= i < height and 0 <= j < width and board[i][j] == 'O':
    #             board[i][j] = 'S'
    #             save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
    #     board[:] = [['XO'[c == 'S'] for c in row] for row in board]


