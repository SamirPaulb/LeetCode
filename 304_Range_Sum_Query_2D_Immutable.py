class NumMatrix(object):
    # https://leetcode.com/articles/range-sum-query-2d-immutable/#approach-3-caching-rows-accepted
    # def __init__(self, matrix):
    #     """
    #     initialize your data structure here.
    #     :type matrix: List[List[int]]
    #     """
    #     if matrix is None or len(matrix) == 0:
    #         return
    #     height, width = len(matrix), len(matrix[0])
    #     self.dp = [[0]* (width + 1) for i in range(height)]
    #     for i in range(height):
    #         for j in range(width):
    #             self.dp[i][j + 1] = self.dp[i][j] + matrix[i][j]
    #
    #
    # def sumRegion(self, row1, col1, row2, col2):
    #     """
    #     sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    #     :type row1: int
    #     :type col1: int
    #     :type row2: int
    #     :type col2: int
    #     :rtype: int
    #     """
    #     sum = 0
    #     for i in range(row1, row2 + 1):
    #         sum += self.dp[i][col2 + 1] - self.dp[i][col1]
    #     return sum

    # caching smarter
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix is None or len(matrix) == 0:
            return
        height, width = len(matrix), len(matrix[0])
        self.dp = [[0]* (width + 1) for i in range(height + 1)]
        for i in range(height):
            for j in range(width):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + \
                                        self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
               self.dp[row2 + 1][col1] + self.dp[row1][col1]




        # Your NumMatrix object will be instantiated and called as such:
        # numMatrix = NumMatrix(matrix)
        # numMatrix.sumRegion(0, 1, 2, 3)
        # numMatrix.sumRegion(1, 2, 3, 4)