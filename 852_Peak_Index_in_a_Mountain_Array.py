class Solution(object):
    # def peakIndexInMountainArray(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     i = 0
    #     while A[i + 1] >= A[i]:
    #         i += 1
    #     return i

    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
