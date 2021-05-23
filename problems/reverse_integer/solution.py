class Solution:
    def reverse(self, x: int) -> int:
        
        s = 0
        n = abs(x)
        while n != 0:
            s = s*10 + n%10
            n = n//10

        if x<0:
            s = -(s)
        if(s<(-2**31) or s>(2**31-1)):
            return 0
        return s
       
        
            
        
        
        # 123