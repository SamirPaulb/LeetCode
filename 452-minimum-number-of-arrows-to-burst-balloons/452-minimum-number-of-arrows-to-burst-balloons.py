# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''
Approch:
1. Sort the segments by the end
2. Put an arrow at the end of the 1-st segment
3. From the 2-nd segment, we check whether the current arrow pass through the current segment, if not add an arrow, put it at the end of the current segment

'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        res = 0
        shot = 0
        for start, end in points:
            if res == 0 or start > shot:
                res += 1
                shot = end
        
        return res
    
    