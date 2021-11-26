class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        i = 0
        while i < len(intervals) - 1:
            a, b = intervals[i], intervals[i + 1]
            if a[-1] >= b[0]:
                intervals[i] = [a[0], max(a[-1], b[-1])]
                intervals.pop(i + 1)
            else:
                i += 1
        
        return intervals
           

'''
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[[1,4],[0,4]]
[[1,4],[2,3]]
[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
'''