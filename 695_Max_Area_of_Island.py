class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # because
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(self.dfs(grid, i, j), ans)
                    # ans = max(self.bfs(grid, i, j), ans)
        return ans

    def dfs(self, grid, i, j):
        # DFS based on stack
        stack = [(i, j)]
        area = 0
        # Stack for DFS
        while stack:
            r, c = stack.pop(-1)
            area += 1
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and grid[nr][nc]):
                    stack.append((nr, nc))
                    grid[nr][nc] = 0
        return area

    # def bfs(self, grid, x, y):
    #     # BFS based on queue
    #     queue = [(x, y)]
    #     area = 0
    #     # Stack for DFS
    #     while queue:
    #         i, j = queue.pop(0)
    #         area += 1
    #         if i - 1 >= 0 and grid[i - 1][j] == 1:
    #             grid[i - 1][j] = 0
    #             queue.append((i - 1, j))
    #         if i + 1 < len(grid) and grid[i + 1][j] == 1:
    #             grid[i + 1][j] = 0
    #             queue.append((i + 1, j))
    #         if j - 1 >= 0 and grid[i][j - 1] == 1:
    #             grid[i][j - 1] = 0
    #             queue.append((i, j - 1))
    #         if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
    #             grid[i][j + 1] = 0
    #             queue.append((i, j + 1))
    #     return area

    # def maxAreaOfIsland(self, grid):
    #     # Recursive DFS
    #     seen = set()
    #     def area(r, c):
    #         if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
    #                 and (r, c) not in seen and grid[r][c]):
    #             return 0
    #         seen.add((r, c))
    #         return (1 + area(r+1, c) + area(r-1, c) +
    #                 area(r, c-1) + area(r, c+1))

    #     return max(area(r, c)
    #                for r in range(len(grid))
    #                for c in range(len(grid[0])))
