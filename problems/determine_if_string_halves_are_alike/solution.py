class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        v = ['a', 'e', 'i', 'o', 'u']
        sl = 0
        sr = 0
        if len(s)%2 ==0:
            for  i in range(int(len(s)/2)):
                if s[i] in v:
                    sl +=1
            for i in range(int(len(s)/2), len(s)):
                if s[i] in v:
                    sr +=1
        return sl ==sr
                