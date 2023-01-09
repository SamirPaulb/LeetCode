class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        res = ""
        while i >= 0 or j >= 0 or carry:
            val = carry
            val += 1 if i >= 0 and a[i] == '1' else 0
            val += 1 if j >= 0 and b[j] == '1' else 0
            if val > 1: carry = 1
            else: carry = 0
            val = val % 2
            res += str(val)
            i -= 1
            j -= 1
        
        return res[::-1]
            