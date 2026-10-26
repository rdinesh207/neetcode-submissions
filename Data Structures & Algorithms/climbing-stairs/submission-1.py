class Solution:
    def climbStairs(self, n: int) -> int:
        l,r=1,1
        for i in range(n-1):
            t = l
            l = r+l
            r = t
        return l
        