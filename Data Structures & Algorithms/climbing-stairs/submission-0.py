class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 1
        for _ in range(n-1):
            f = f1
            f1 += f2
            f2 = f
        return f1