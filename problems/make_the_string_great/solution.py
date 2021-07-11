class Solution:
    def makeGood(self, s):
        s = list(s)
        ans = [s[0]]
        s.pop(0)
        for i in range(len(s)):
            if len(ans) != 0 and abs(ord(ans[-1]) - ord(s[0])) == 32:
                ans.pop(-1)
                s.pop(0)
            else:
                ans.append(s[0])
                s.pop(0)
            
        res = ""
        for i in ans:
            res += i
            
        return res