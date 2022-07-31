class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        tmp = a
        while len(a) < len(b):
            a += tmp
            res += 1
        if self.subStr(a, b):
            return res
        if self.subStr(a+tmp, b):
            return res + 1
        return -1
    
    
    def subStr(self, a, b):  # check if b is substring of a 
        for i in range(len(a)):
            if a[i] == b[0] and i+len(b) <= len(a) and a[i:i+len(b)] == b:
                return True
        return False

    