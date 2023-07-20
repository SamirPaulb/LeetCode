class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sa = []
        for i in range(len(s)):
            if s[i] == '#':
                if sa: sa.pop()
            else:
                sa.append(s[i])
        ta = []
        for i in range(len(t)):
            if t[i] == '#':
                if ta: ta.pop()
            else:
                ta.append(t[i])
        
        return ''.join(sa) == ''.join(ta)