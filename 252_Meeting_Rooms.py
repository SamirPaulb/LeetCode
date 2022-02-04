# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # def canAttendMeetings(self, intervals):
    #     """
    #     :type intervals: List[Interval]
    #     :rtype: bool
    #     """
    #     # if start then count += 1
    #     # if end then count -= 1
    #     # if count >= 2, then False
    #     check = []
    #     for it in intervals:
    #         check.append((it.start, True))
    #         check.append((it.end - 1, False))
    #     check.sort(key=lambda x : x[0])
    #     count = 0
    #     for t in check:
    #         if t[1]:
    #             count += 1
    #             if count > 1:
    #                 return False
    #         else:
    #             count -= 1
    #     return True

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)
        ls = len(intervals)
        for i in range(ls - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
