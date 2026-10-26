class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, n in enumerate(nums):
            index[n]=i
        for i,n in enumerate(nums):
            if (target-n) in nums and i!=index[target-n]:
                return [i, index[target-n]]



        