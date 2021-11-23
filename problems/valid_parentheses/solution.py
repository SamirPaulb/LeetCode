class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if len(stack) == 0: 
                stack.append(s[i])
                i += 1
                continue
            if stack[-1] == "(" and s[i] == ")" or stack[-1] == "{" and s[i] == "}" or stack[-1] == "[" and s[i] == "]":
                stack.pop()
            
            else:
                stack.append(s[i])
            
            i += 1
        
        return len(stack) == 0