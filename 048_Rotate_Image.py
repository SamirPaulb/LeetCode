class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # rotate from outside to inside
        if matrix is None or len(matrix) == 1:
            return
        ls = len(matrix)
        for i in range(ls / 2):
            # border
            begin, end = i, ls - 1 - i
            for k in range(ls - 2 * i - 1):
                temp = matrix[end - k][begin]
                matrix[end - k][begin] = matrix[end][end - k]
                matrix[end][end - k] = matrix[begin + k][end]
                matrix[begin + k][end] = matrix[begin][begin + k]
                matrix[begin][begin + k] = temp
        return

if __name__ == '__main__':
    # begin
    s = Solution()
    s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])




