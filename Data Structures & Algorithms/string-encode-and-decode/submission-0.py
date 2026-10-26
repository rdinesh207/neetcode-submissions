class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            x+=f"{len(s)}#"+s
        return x

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        j = 0

        while i<len(s):
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            l.append(s[i:j])
            i = j

        return l

        