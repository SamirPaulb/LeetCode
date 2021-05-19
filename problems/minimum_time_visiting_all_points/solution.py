class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        a = 0
        for i in range(len(points)-1):
            a += max(abs(points[i+1][0]- points[i][0]), abs(points[i+1][1]- points[i][1]))
        return a
            