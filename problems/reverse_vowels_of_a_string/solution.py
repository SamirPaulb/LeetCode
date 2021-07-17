class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        f = 0
        l = len(s)-1
        vou = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while f < l:
            if (s[f] in vou) and (s[l] in vou):
                s[f], s[l] = s[l], s[f]
                f +=1
                l -= 1
            elif s[f] in vou and s[l] not in vou:
                l -= 1
            elif s[f] not in vou and s[l] in vou:
                f += 1
            else:
                f += 1
                l -= 1
        ans = ""
        for  i in s:
            ans += i
        return ans