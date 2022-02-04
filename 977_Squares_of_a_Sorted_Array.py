class Solution(object):
    # def sortedSquares(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: List[int]
    #     """
    #     # Directly sort
    #     return sorted(x * x for x in A) 

    def sortedSquares(self, A):
        pos = 0
        while pos < len(A) and A[pos] < 0:
            pos += 1
        # pos point to first positve
        # npos point to larget negative
        npos = pos - 1
        res = []
        while pos < len(A) and npos >= 0:
            if A[npos] ** 2 < A[pos] ** 2:
                res.append(A[npos] ** 2)
                npos -= 1
            else:
                res.append(A[pos] ** 2)
                pos +=1 
        while npos >= 0:
            res.append(A[npos] ** 2)
            npos -= 1
        while pos < len(A):
            res.append(A[pos] ** 2)
            pos += 1
        return res
