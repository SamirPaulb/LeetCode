class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        cp = points[0][1]
        res = 1
        for point in points[1:]:
            if point[0] > cp:
                res += 1
                cp = point[1]
        
        return res