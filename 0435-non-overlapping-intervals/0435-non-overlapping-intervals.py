class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        cur = intervals[0]
        res = 0
        for new in intervals[1:]:
            if new[0] < cur[1]:
                res += 1
                if new[1] < cur[1]:
                    cur = new
            else:
                cur = new
        
        return res