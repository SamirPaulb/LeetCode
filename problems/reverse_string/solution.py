class Solution:
    def reverseString(self, s: List[str]) -> None:
        a = 0
        b = len(s)-1
        while a< b:
            s[a], s[b] = s[b] , s[a]
            a += 1
            b -= 1