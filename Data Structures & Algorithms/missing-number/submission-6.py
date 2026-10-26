class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = sum(range(max(nums)+1))
        return s2-s1 if (s2-s1>0 or 0 not in nums) else max(nums)+1
        