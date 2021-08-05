class Solution:
    def countSubstrings(self, s: str) -> int:
        a = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                a.append(s[i:j+1])
        
        count = 0
        for i in a:
            if i == i[::-1]:
                count += 1
        
        return count
            