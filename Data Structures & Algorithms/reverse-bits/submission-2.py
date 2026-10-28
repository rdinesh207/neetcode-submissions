class Solution:
    def reverseBits(self, n: int) -> int:
        u = list(bin(n).split("b")[-1])
        u.reverse()
        u = u + ['0']*(32-len(u))
        # print(u)
        m = int("".join(u),2)
        return m
        