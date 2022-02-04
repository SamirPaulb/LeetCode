class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # m * n temp array
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        # Compute final location
        true_k = k % (m * n)
        # row move
        move_i = true_k / n
        # col move
        move_j = true_k % n

        for i in range(m):
            for j in range(n):
                new_i = i + move_i
                # move one row if move_j + j >= n
                if move_j + j >= n:
                    new_i += 1
                new_i %= m
                new_j = (j + move_j) % n
                new_grid[new_i][new_j] = grid[i][j]
        return new_grid
