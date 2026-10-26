class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mx, mn = 1,1

        for n in nums:
            t = n*mx
            mx = max(t, n*mn, n)
            mn = min(t, n*mn, n)
            res = max(res, mx)
        return res
        