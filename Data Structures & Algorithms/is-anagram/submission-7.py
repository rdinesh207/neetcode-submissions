class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*26
        m = [0]*26
        for c in s:
            l[ord(c)-ord("a")]+=1
        
        for c in t:
            m[ord(c)-ord("a")]+=1
        
        for i in range(26):
            if l[i]!=m[i]:
                return False
        
        return True