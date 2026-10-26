class Solution:
    def isValid(self, s: str) -> bool:
        t = ""
        u = {"}":"{", "]":"[", ")":"("}
        c = 0
        for i in s:
            if i in u.values():
                t+=i
                c+=1
            elif len(t)>0 and i in u.keys():
                if u[i]==t[-1]:
                    t=t[:-1]
                else:
                    return False
        if len(t)==0 and (c*2)==len(s):
            return True
        else:
            return False
        