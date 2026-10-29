class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(list(map(int, list(bin(n).split("b")[-1]))))
        