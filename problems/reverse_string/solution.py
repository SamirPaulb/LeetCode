class Solution:
    def reverseString(self, s: List[str]) -> None:
        def rev(l, r, s):
            if l >= r: return
            s[l], s[r] = s[r], s[l]
            rev(l+1, r-1, s)
            
        return rev(0, len(s)-1, s)
        