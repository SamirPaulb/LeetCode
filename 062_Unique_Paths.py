class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dmap = [[0] * n for _ in range(m)]
        for i in range(m):
            dmap[i][0] = 1
        for j in range(n):
            dmap[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                l = u = 0
                if i-1 >= 0:
                    u = dmap[i-1][j]
                if j-1>= 0:
                    l = dmap[i][j-1]
                dmap[i][j] = l + u
        return dmap[m-1][n-1]
