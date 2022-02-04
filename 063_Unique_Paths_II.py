class Solution(object):
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     dmap = [[0] * n for _ in range(m)]
    #     for i in range(m):
    #         if obstacleGrid[i][0] != 1:
    #             dmap[i][0] = 1
    #         else:
    #             break
    #     for j in range(n):
    #         if obstacleGrid[0][j] != 1:
    #             dmap[0][j] = 1
    #         else:
    #             break
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if obstacleGrid[i][j] == 1:
    #                 continue
    #             l = u = 0
    #             if i - 1 >= 0:
    #                 u = dmap[i - 1][j]
    #             if j - 1 >= 0:
    #                 l = dmap[i][j - 1]
    #             dmap[i][j] = l + u
    #     return dmap[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0:
            return 0
        dmap = [[0] * (n + 1) for _ in range(m + 1)]
        dmap[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in  range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dmap[i][j] = 0
                else:
                    dmap[i][j] = dmap[i][j + 1] + dmap[i + 1][j]
        return dmap[0][0]