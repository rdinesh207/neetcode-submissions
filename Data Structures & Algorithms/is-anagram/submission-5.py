class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d[c]+1 if c in d else 1
        # print(d)
        for c in t:
            if c not in d:
                return False
            else:
                d[c] = d[c]-1
                if d[c]<0:
                    return False
        # print(d)
        if sum(d.values())>0:
            return False
        return True
        
        