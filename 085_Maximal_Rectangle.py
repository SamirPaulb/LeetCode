class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/6650/share-my-dp-solution/2
        if matrix is None or len(matrix) == 0:
            return 0
        ls_row, ls_col = len(matrix), len(matrix[0])
        left, right, height = [0] * ls_col, [ls_col] * ls_col, [0] * ls_col
        maxA = 0
        for i in range(ls_row):
            curr_left, curr_right = 0, ls_col
            for j in range(ls_col):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(ls_col):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                else:
                    left[j], curr_left = 0, j + 1
            for j in range(ls_col - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j], curr_right = ls_col, j
            for j in range(ls_col):
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        return maxA



