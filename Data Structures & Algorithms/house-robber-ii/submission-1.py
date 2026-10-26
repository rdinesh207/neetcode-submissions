class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            r1, r2 = 0,0
            for n in nums:
                newr = max(n+r1, r2)
                r1 = r2
                r2 = newr
            return r2
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])

        