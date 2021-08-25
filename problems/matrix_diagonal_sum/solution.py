class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
        i = 0
        j = len(mat) - 1
        while j >= 0 and i < len(mat):
            if i != j:
                s += mat[i][j]
            i += 1
            j -= 1
        return s