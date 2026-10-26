class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i, n in enumerate(nums):
            ind[n] = i
        for i, n in enumerate(nums):
            dif = target - n
            if dif in ind and ind[dif]!=i:
                return [i, ind[dif]]
        return []

        