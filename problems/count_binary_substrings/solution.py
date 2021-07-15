class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        grp = []
        n = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                n += 1
            else:
                grp.append(n)
                n = 1
        grp.append(n)
        print(grp)
        ans = 0
        for i in range(1,len(grp)):
            ans += min(grp[i-1], grp[i])
        return ans
    
    