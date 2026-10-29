class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            l = map(int, list(str(n)))
            p = 0
            # print(l)
            for i in l:
                p+=i*i
            return p
        s = []
        while True:
            n = sos(n)
            if n==1:
                return True
            elif n in s:
                break
            s.append(n)
        return False
        