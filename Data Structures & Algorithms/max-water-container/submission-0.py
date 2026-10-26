class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights)-1
        area = 0
        while first<last:
            if heights[first]<heights[last]:
                a = (last-first)*heights[first]
                first+=1
            else:
                a = (last-first)*heights[last]
                last-=1
            
            area = a if a>area else area
        return area

        