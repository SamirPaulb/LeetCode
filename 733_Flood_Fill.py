class Solution(object):
    # def floodFill(self, image, sr, sc, newColor):
    #     """
    #     :type image: List[List[int]]
    #     :type sr: int
    #     :type sc: int
    #     :type newColor: int
    #     :rtype: List[List[int]]
    #     """
    #     r_ls, c_ls = len(image), len(image[0])
    #     color = image[sr][sc]
    #     if color == newColor:
    #         return image

    #     def dfs(r, c):
    #         if image[r][c] == color:
    #             image[r][c] = newColor
    #             if r - 1 >= 0: dfs(r - 1, c)
    #             if r + 1 < r_ls: dfs(r + 1, c)
    #             if c - 1 >= 0: dfs(r, c - 1)
    #             if c + 1 < c_ls: dfs(r, c + 1)

    #     dfs(sr, sc)
    #     return image

    def floodFill(self, image, sr, sc, newColor):
        # BFS with queue
        r_ls, c_ls = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        queue = [(sr, sc)]
        while len(queue) > 0:
            r, c = queue.pop(0)
            if image[r][c] == color:
                image[r][c] = newColor
                if r - 1 >= 0: queue.append((r - 1, c))
                if r + 1 < r_ls: queue.append((r + 1, c))
                if c - 1 >= 0: queue.append((r, c - 1))
                if c + 1 < c_ls: queue.append((r, c + 1))
        return image
