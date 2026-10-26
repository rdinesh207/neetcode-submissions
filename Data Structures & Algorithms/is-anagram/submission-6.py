class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for c in s:
            d1[c]=d1.get(c,0)+1
        for c in t:
            if c in d1:
                d1[c]-=1 if d1[c]>0 else 0
            else:
                return False
        return sum(d1.values())==0