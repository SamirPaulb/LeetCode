class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        
        b = int(s)
        b += 1
        s = str(b)
        a = []
        for i in range(len(s)):
            a.append(s[i])
        return a
            
            
    