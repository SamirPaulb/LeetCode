class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique = set()
        for i in range(k-1, len(s)):
            sb = s[i-k+1:i+1]
            unique.add(sb)
        return len(unique) == 2**k