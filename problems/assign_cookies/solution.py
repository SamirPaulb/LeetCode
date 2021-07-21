class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gi, si = 0, 0
        g.sort()
        s.sort()
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
                si += 1
            else:
                si += 1
        return gi
    
    