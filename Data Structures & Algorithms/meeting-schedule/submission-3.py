"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        blocked = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start in blocked or end in blocked:
                return False
            blocked += range(start, end)
        return True