class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numss = set(nums)
        x = min(nums)-1
        length = 1
        m = 0
        for n in numss:
            if n-1 not in numss:
                lent=1
                while n+lent in numss:
                    lent+=1
                m=max(m,lent)
        return m