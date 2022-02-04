class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solution/
        def enough(x):
            count = 0
            # ith row [i, 2*i, 3*i, ..., n*i]
            # for each column, k = x // i
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
