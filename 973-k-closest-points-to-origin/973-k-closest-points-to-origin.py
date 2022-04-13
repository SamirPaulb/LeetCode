class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            val = points[i][0] ** 2 + points[i][1] ** 2
            points[i].append(val)
        
        points.sort(key = lambda x:x[2])
        
        res = []
        for i in range(k):
            res.append(points[i][:2])
        
        return res