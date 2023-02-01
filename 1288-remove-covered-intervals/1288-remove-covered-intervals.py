class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]), reverse = True)
        stack = []
        cnt = 0
        for l, r in intervals:
            while stack and l <= stack[-1][0] and stack[-1][1] <= r:
                stack.pop()
                cnt += 1
            stack.append((l,r))
        # print(intervals, cnt)
        return len(intervals) - cnt
        