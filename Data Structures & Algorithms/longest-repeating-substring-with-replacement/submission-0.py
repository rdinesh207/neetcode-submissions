class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        l = 0
        mx = 0

        for r in range(len(s)):
            h[s[r]] = 1+h.get(s[r],0)
            mx = max(mx, h[s[r]])
            if (r-l+1)-mx>k:
                h[s[l]]-=1
                l+=1
        return (r-l+1)
        