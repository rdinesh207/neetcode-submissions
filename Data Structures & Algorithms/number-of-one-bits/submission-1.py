class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n!=0:
            sum+=n%2
            n//=2
        return sum
        