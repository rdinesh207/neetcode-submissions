class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        res = 0
        for p in prices:
            if p<l:
                l = p
            res = max(res, p-l)
        return res




        