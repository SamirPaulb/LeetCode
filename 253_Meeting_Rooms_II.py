# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# class Solution(object):
#     def minMeetingRooms(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: int
#         """
#         # If there is no meeting to schedule then no room needs to be allocated.
#         if not intervals:
#             return 0
#         # The heap initialization
#         free_rooms = []
#         # Sort the meetings in increasing order of their start time.
#         intervals.sort(key= lambda x: x.start)
#         # Add the first meeting. We have to give a new room to the first meeting.
#         heapq.heappush(free_rooms, intervals[0].end)
#         # For all the remaining meeting rooms
#         for i in intervals[1:]:
#             # If the room due to free up the earliest is free, assign that room to this meeting.
#             if free_rooms[0] <= i.start:
#                 heapq.heappop(free_rooms)
#             # If a new room is to be assigned, then also we add to the heap,
#             # If an old room is allocated, then also we have to add to the heap with updated end time.
#             heapq.heappush(free_rooms, i.end)
#         # The size of the heap tells us the minimum rooms required for all the meetings.
#         return len(free_rooms)


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        timeline = []
        for interval in intervals:
            # meeting root + 1
            timeline.append((interval.start, 1))
            # meeting root - 1
            timeline.append((interval.end, -1))
        # sort by time
        timeline.sort()
        ans = curr = 0
        # go through timeline
        for _, v in timeline:
            curr += v
            # max meeting room used at this point
            ans = max(ans, curr)
        return ans
