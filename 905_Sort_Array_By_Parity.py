class Solution(object):
    # def sortArrayByParity(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: List[int]
    #     """
    #     # Bad idea, O(nlogn)
    #     A.sort(key=lambda x: x % 2)
    #     return A

    # def sortArrayByParity(self, A):
    #     return ([x for x in A if x % 2 == 0] +
    #             [x for x in A if x % 2 == 1])

    def sortArrayByParity(self, A):
        # Quit like quick sort or quick selection
        lo, hi = 0, len(A) - 1
        while lo < hi:
            if A[lo] % 2 > A[hi] % 2:
                A[lo], A[hi] = A[hi], A[lo]
            if A[lo] % 2 == 0: lo += 1
            if A[hi] % 2 == 1: hi -= 1
        return A
