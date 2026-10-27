class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        r = 0
        for i in range(len(digits)-1, -1, -1):
            r = (digits[i]+c)%10
            c = (digits[i]+c)//10
            digits[i]=r
        if c:
            return [c]+digits
        else:
            return digits
        