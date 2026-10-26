class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {i:0 for i in nums}
        for i in nums:
            d[i]+=1
        for i in d.keys():
            d[i]-=1
        return True if sum(d.values()) else False
         