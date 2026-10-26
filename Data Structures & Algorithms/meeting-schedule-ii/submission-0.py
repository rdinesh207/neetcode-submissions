"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        l = []
        for item in intervals:
            l.append((item.start, 1))
            l.append((item.end, -1))
        l.sort(key=lambda x:(x[0], x[1]))
        max_count = 0
        count = 0
        for item in l:
            count+=item[-1]
            max_count = max(max_count, count)
        return max_count
                        
                
        