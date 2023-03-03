class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack); n = len(needle)
        for i in range(h):
            if haystack[i] == needle[0] and haystack[i:i+n] == needle: return i
        
        return -1