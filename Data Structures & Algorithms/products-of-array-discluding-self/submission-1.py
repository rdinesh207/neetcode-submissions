class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        q = 1
        z = len(nums)
        for i in nums:
            p*=i
            if i!=0:
                q*=i
                z-=1
        for i,x in enumerate(nums):
            if z<=1:
                if nums[i]==0 and p==0:
                    nums[i]=q
                else:
                    nums[i]=p//x
            else:
                return [0]*len(nums)
        return nums
        
        