class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        i = len(num1)-1; j = len(num2)-1
        while i >= 0 or j >= 0 or carry:
            val = carry
            val += ord(num1[i]) - ord("0") if i >= 0 else 0
            val += ord(num2[j]) - ord("0") if j >= 0 else 0 
            carry = val // 10
            val = val % 10
            res = chr(ord("0") + val) + res
            i -= 1
            j -= 1
        
        return res