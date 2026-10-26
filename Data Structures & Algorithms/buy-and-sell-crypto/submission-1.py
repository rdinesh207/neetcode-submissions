class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        mins = prices[0]
        for s in prices:
            maxp = max(s-mins, maxp)
            mins = min(mins, s)
        return maxp




        