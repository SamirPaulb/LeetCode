class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = []
        num_row = len(mat)
        num_col = len(mat[0])
        col = 0
        flag = 1
        while col < num_col and flag:
            for i in range(num_row):
                if i in res:
                    continue
                # Add first row with 0 into res
                if mat[i][col] == 0:
                    res.append(i)
                if len(res) == k:
                    flag = 0
                    break
            col += 1
        if len(res) == k:
            return res
        # if res less than k
        for i in range(num_row):
            if i in res:
                continue
            res.append(i)
            if len(res) == k:
                break
        return res