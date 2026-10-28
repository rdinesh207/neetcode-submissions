class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums)-1
        while f<=l:
            m = ((l-f)//2) + f
            if nums[m]==target:
                return m
            elif nums[m]<target:
                f = m+1
            else:
                l = m-1
        return -1
        