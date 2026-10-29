class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        m = 0
        for l in range(len(prices)-1):
            for r in range(l+1, len(prices)):
                m = max(m, prices[r]-prices[l])
        return m

        