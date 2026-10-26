class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        maxc = 0
        for n in s:
            if n-1 not in s:
                count=1
                while n+count in s:
                    count+=1
                maxc = max(count, maxc)
        return maxc
        