class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.findall("[A-Z\d]", s, re.I)
        v = s.copy()
        v.reverse()
        print(s,v)
        x = 0
        for i,j in zip(s,v):
            x+=i==j
        if x==len(s):
            return True
        else:
            return False

        