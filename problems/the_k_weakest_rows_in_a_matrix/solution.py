class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a = []
        for i in range(len(mat)):
            a.append(mat[i].count(1))
        ans = []
        for i in range(k):
            ans.append(a.index(min(a)))
            a[a.index(min(a))] = 2**31
        return ans