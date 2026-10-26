class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {i:0 for i in s}
        t1 = {i:0 for i in t}
        for i in s:
            s1[i]+=1
        for i in t:
            if i in s1.keys():
                s1[i]-=1
            else: return False
        x = True
        for i in s1.values():
            x = x and i==0
        return x
        