class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        newl = [intervals[0]]
        for i in range(1, len(intervals)):
            if newl[-1][-1]>=intervals[i][0]:
                if newl[-1][-1]<=intervals[i][-1]:
                    newl[-1][-1]=intervals[i][-1]
            else:
                newl.append(intervals[i])
        return newl
            
        