class Solution(object):
    # def kClosest(self, points, K):
    #     """
    #     :type points: List[List[int]]
    #     :type K: int
    #     :rtype: List[List[int]]
    #     """
    #     # Sort
    #     return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]
    
    def kClosest(self, points, K):
        # K smallest heaq
        return heapq.nsmallest(K, points, key=lambda x: x[0] ** 2 + x[1] ** 2)
