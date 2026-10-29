class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones)>1 and stones[1]:
            val = abs(stones[0]-stones[1])
            stones[0], stones[1] = 0, val
            stones.sort(reverse=True)
        return stones[0]


        