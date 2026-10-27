class Solution:
    def countBits(self, n: int) -> List[int]:

        def count(m):
            s = 0
            while m:
                s+=m%2
                m//=2
            return s
        return list(map(count, range(n+1)))



        