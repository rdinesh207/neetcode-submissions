class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in "[({":
                l.append(c)
            else:
                if not l or l.pop(-1)!=d[c]:
                    return False
        return True if len(l)==0 else False

            

        