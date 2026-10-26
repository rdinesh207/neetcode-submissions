class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        l = [intervals[0]]

        for start, end in intervals:
            lastend = l[-1][1]

            if start<=lastend:
                l[-1][1] = max(lastend, end)
            else:
                l.append([start, end])
        return l

        