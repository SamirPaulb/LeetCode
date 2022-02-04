class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # because
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)

    # def findCircleNum(self, M):
    #     # BFS
    #     visited = [0] * len(M)
    #     count = 0
    #     queue = []
    #     for i in range(len(M)):
    #         if visited[i] == 0:
    #             queue.append(i)
    #             while queue:
    #                 curr = queue.pop(0)
    #                 visited[curr] = 1
    #                 for j in range(len(M)):
    #                     if M[curr][j] == 1 and visited[j] == 0:
    #                         queue.append(j)
    #             count += 1
    #     return count

#     def findCircleNum(self, M):
#         # Union Find
#         union = Union()
#         for i in range(len(M)):
#             union.add(i)
#         for i in range(len(M)):
#             for j in range(i + 1, len(M)):
#                 if M[i][j] == 1:
#                     union.union(i, j)
#         return union.count

# class Union(object):
#     """
#     weighted quick union find
#     """
#     def __init__(self):
#         # both dic and list is fine
#         self.id = {}
#         self.sz = {}
#         self.count = 0

#     def count(self):
#         return self.count

#     def connected(self, p, q):
#         return self.find(p) == self.find(q)

#     def add(self, p):
#         # init
#         self.id[p] = p
#         self.sz[p] = 1
#         self.count += 1

#     def find(self, p):
#         """
#         find root of p, and compress path
#         """
#         while p != self.id[p]:
#             self.id[p] = self.id[self.id[p]]
#             p = self.id[p]
#         return p

#     def union(self, p, q):
#         """
#         connect p and q
#         """
#         i, j = self.find(p), self.find(q)
#         if i == j:
#             return
#         if self.sz[i] > self.sz[j]:
#             i, j = j, i
#         self.id[i] = j
#         self.sz[j] += self.sz[i]
#         self.count -= 1
