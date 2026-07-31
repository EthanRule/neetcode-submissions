"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)



        for i, item in enumerate(intervals, start=1):

            if i >= len(intervals):
                break

            if intervals[i - 1].end > intervals[i].start:
                return False

        return True