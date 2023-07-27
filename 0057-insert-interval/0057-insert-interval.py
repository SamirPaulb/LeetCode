class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if newInterval[0] <= intervals[0][0]:
            intervals = [newInterval] + intervals
        else:
            taken = False
            for i in range(len(intervals)-1):
                if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i+1][0]:
                    intervals = intervals[:i+1] + [newInterval] + intervals[i+1:]
                    taken =  True
                    break
            if not taken: intervals += [newInterval]
        # print(intervals)
        res = []
        for cur in intervals:
            if not res: 
                res.append(cur)
            else:
                if cur[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], cur[1])
                else:
                    res.append(cur)
        return res