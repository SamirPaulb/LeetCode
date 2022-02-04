class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution
        row_num = len(grid)
        if row_num == 0 || len(grid[0]) == 0:
            return 0
        islands, overlaps = 0, 0
        col_num = len(grid[0])
        for i in range(row_num):
            for j in range(col_num):
                if (grid[i][j] == 1):
                    islands += 1
                    # careful about right and down
                    if (i < row_num - 1 && grid[i + 1][j] == 1):
                        overlaps += 1
                    if (j < col_num - 1 && grid[i][j + 1] == 1):
                        overlaps += 1
        return islands * 4 - overlaps * 2
