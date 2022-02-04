class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        queue = [(0, 0), (-1, -1)]
        visited = set()
        isSuccess = False
        index = 0
        while len(queue) != 1 or queue[0][0] != -1:
            p = queue.pop(0)
            if p[0] == len(s1) and p[1] == len(s2):
                return True
            if p[0] == -1:
                queue.append(p)
                index += 1
                continue
            if p in visited:
                continue
            visited.add(p)
            if p[0] < len(s1):
                if s1[p[0]] == s3[index]:
                    queue.append((p[0] + 1, p[1]))
            if p[1] < len(s2):
                if s2[p[1]] == s3[index]:
                    queue.append((p[0], p[1] + 1))
        return False
