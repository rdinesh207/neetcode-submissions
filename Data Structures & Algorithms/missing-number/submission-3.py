class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m1 = max(nums)
        i = 0
        for i in range(0,m1+1):
            if i not in nums:
                return i
        return i+1
        

        # for i in range(len(nums)-1):
        #     if nums[i+1]-nums[i]>1:
        #         return nums[i]+1
        