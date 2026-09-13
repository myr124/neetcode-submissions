"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''

we have an array intervals and return a boolean where we
return true if people can attend all intervals without overlap
false otherwise

0,30 5,10

start2 >= start1 and start2 < end2

start = 0
end = 30

'''

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals:
            return True
        
        start = intervals[0].start
        end = intervals[0].end
        
        for i in range(1,len(intervals)):
            if intervals[i].start >= start and intervals[i].start < end:
                return False
            
            start = intervals[i].start
            end = intervals[i].end
        
        return True
            