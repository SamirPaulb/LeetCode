class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda X : X[0])  # Sort intervals 0-th column wise. 
        #print(intervals)
        l, r = 0, 1
        while r < len(intervals):
            if intervals[r][0] <= intervals[l][1]:
                intervals[r] = [intervals[l][0], max(intervals[l][1], intervals[r][1])]
                intervals.pop(l)
            else:
                r += 1
                l += 1
        
        return intervals