class Solution:
    def reverseBits(self, n: int) -> int:
        b = 0
        for _ in range(32):
            b*=2
            b+=n%2
            n//=2
        return b

        