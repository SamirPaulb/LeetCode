class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def findRedundantConnection(self, edges):
        N = len(set(chain(*edges)))
        dsu = DSU(N)
        for i, j in edges:
            if dsu.find(i-1) == dsu.find(j-1):
                return([i,j])
            else:
                dsu.union(i-1,j-1)