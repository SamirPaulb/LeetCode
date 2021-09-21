class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        for row in matrix:
            for i in row:
                a.append(i)
        a.sort()
        return a[k-1]