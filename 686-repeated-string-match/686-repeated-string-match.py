class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(b) // len(a)
        if self.subStr(a*n, b): return n
        if self.subStr(a*(n+1), b): return n+1
        if self.subStr(a*(n+2), b): return n+2    
        return -1
    
    ''' 
    def subStr(self, a, b):
        return b in a
    '''
    def subStr(self, a, b):  # check if b is substring of a or not
        for i in range(len(a)):
            if a[i] == b[0] and i+len(b) <= len(a) and a[i:i+len(b)] == b:
                return True
        return False

