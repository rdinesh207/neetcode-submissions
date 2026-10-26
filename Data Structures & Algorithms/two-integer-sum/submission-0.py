class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target==nums[i]+nums[j]:
                    m = [i,j]
                    break
            if m:
                    break
        return m


        