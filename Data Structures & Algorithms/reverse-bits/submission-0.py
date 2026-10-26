class Solution:
    def reverseBits(self, n: int) -> int:
        y = 0
        for i in range(32):
            y=y+((n%2)*(2**(32-i)))
            n//=2
        return y//2

        