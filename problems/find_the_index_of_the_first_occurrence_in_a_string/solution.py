class Solution:
    def strStr(self, haystack, needle):
        h= len(haystack)
        n = len(needle)
        if n>h:
            return -1
        
        elif n == 0:
            return 0
        
        for i in range(h-n+1):
            s = 0
            for j in range(n):
                if haystack[i+j] == needle[j]:
                    s +=1
            if s == n:
                return i
        return -1