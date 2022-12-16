# https://www.vedantu.com/question-answer/find-the-area-of-the-triangle-whose-vertices-are-class-11-maths-cbse-5f8309d2ed668270c0bf8f07

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
                    res = max(res, area)
        
        return res