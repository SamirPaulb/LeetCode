class Solution:
    def findKthPositive(self, A, k):
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k