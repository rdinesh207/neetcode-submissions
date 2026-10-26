class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, l, t):
            if t==target:
                res.append(l.copy())
                return
            elif t>target: return
            elif i>=len(nums): return
            l.append(nums[i])
            dfs(i, l, t+nums[i])
            l.pop()
            dfs(i+1, l, t)
            return
        
        dfs(0, [], 0)
        return res
            
        