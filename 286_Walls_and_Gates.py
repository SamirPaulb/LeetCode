class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # BFS with queue
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        q = []
        for row in range(m):
            for col in range(n):
                # gate
                if rooms[row][col] == 0:
                    q.append((row, col))

        while len(q) > 0:
            point = q.pop(0)
            row, col = point[0], point[1]
            for d in direction:
                r = row + d[0]
                c = col + d[1]
                # wall or out of rooms
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != 2147483647:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                q.append((r, c))
