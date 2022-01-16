class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        n = columnNumber
        while n > 0:
            if n % 26 != 0:
                char = chr(64 + n%26)
                res.append(char)
                n -= n %26
                n = n//26
                
            else:
                res.append("Z")
                n -= 26
                n = n//26
        
        res.reverse()
        print(res)
        return "".join(res)
        
        