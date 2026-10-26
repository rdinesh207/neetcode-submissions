class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        ct, win = {}, {}
        for c in t:
            ct[c]=1+ct.get(c, 0)
        res, resl = [-1,-1], float("inf")
        have, need = 0, len(ct)
        l = 0
        for r in range(len(s)):
            c = s[r]
            win[c]=1+win.get(c,0)
            if c in t and win[c]==ct[c]:
                have+=1
            while have==need:
                if (r-l+1)<resl:
                    res = [l,r]
                    resl = r-l+1
                win[s[l]]-=1
                if s[l] in t and win[s[l]]<ct[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resl !=float("inf") else ""

        