class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.findall("[\da-z]", s.lower())
        t = tuple(s.copy())
        s.reverse()
        print(s,t)
        if tuple(s)==t:
            return True
        else:
            return False

        