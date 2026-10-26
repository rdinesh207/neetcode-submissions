class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {i:0 for i in nums}
        for i in nums:
            d[i]+=1
        y = list(d.items())
        y.sort(key=lambda x:x[-1], reverse=True)
        l = []
        for i in range(k):
            l.append(y[i][0])
        return l

        