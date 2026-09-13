"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
'''
prev meeting rooms we found a solution to find conflict

start2 >= start1 and start2 < end1 means theres conflict

Note: (0,8),(8,10) is NOT considered a conflict at 8.

we should also probably keep a running max of end time

'''


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        
        s,e = 0,0

        res = 0
        count = 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        while s < len(start):

            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(count,res)

        return res
