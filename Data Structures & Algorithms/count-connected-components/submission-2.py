class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = set()
        d = {}
        for e in edges:
            if e[0] not in d and e[0] not in p:
                d[e[0]]=[e[1]]
                # l.append(e[1])
            else:
                if e[0] in d:
                    d[e[0]].append(e[1])
                    if e[1] in d:
                        d[e[0]]+=d.pop(e[1])
                else:
                    f = -1
                    for x in d:
                        if e[0] in d[x]:
                            f = x
                            break
                    d[f].append(e[1])
                    if e[1] in d:
                        d[f]+=d.pop(e[1])
            p.add(e[0])
            p.add(e[1])
        print(p,d)
        return (n-len(p))+len(d)


        