class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i]=d.get(i, 0)+1
        l = [[d[i], i] for i in d]
        l.sort(key=lambda x:x[0])
        return [i[1] for i in l[-k:]]
        
        