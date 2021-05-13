class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        a = 0
        stack = []
        
        stack.append(s[0])
        i = 1
        while i < len(s):
            
            
            if stack[len(stack)-1] != s[i]:
                stack.pop()
            
            if len(stack) !=0:    
                if stack[len(stack)-1] == s[i]:
                    stack.append(s[i])

                
            if len(stack) ==0:
                a = a+1
                i = i+1
                if i<len(s):
                    stack.append(s[i])
            i = i+1
            
        return a
                
                
            
        