class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        a = re.findall("[A-Z\d]", s, re.I)
        b = a.copy()
        b.reverse()
        if a==b:
            return True
        else:
            return False
        