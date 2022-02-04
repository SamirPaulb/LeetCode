class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
        # Alternative Solution:
        # return zip(*A)

    # def transpose(self, A):
    #     res = []
    #     for i in range(len(A[0])):
    #         temp = []
    #         for j in range(len(A)):
    #             temp.append(A[j][i])
    #         res.append(temp)
    #     return res
