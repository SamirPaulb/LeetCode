class Solution(object):
    # def fixedPoint(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     for index, value in enumerate(A):
    #         # Because if A[i] > i, then i can never be greater than A[i] any more
    #         if index == value:
    #             return index
    #         elif index < value:
    #             return -1

    def fixedPoint(self, A):
        l, h = 0, len(A) - 1
        while l <= h:
            mid = (l + h) // 2
            if A[mid] < mid:
                l = mid + 1
            elif A[mid] > mid:
                h = mid - 1
            else:
                return mid
        return -1
