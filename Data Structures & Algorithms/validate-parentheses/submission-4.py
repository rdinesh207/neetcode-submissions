class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maap = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack)>0 and maap[c]==stack[-1]:
                stack.pop(-1)
            else:
                return False
        if len(stack)==0:
            return True
        return False

        