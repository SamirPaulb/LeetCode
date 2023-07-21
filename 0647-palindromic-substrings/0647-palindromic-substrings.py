class Solution:
    def countSubstrings(self, s: str) -> int:
        def palCount(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        return sum(palCount(i, i) + palCount(i, i+1) for i in range(len(s)))