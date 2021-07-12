class Solution:
    def isValid(self, s: str) -> bool:
        m1 = {"(" : 0, "{" : 1, "[" : 2}
        m2 = {")" : 0, "}" : 1, "]" : 2}
        stack = []
        for i in range(len(s)):
            if ((len(stack) == 0 and s[i] in m2) 
               or (s[i] in m2 and stack[-1] in m1 
                   and m1[stack[-1]] != m2[s[i]])) :
                return False
            elif (s[i] in m2 and stack[-1] in m1 
                   and m1[stack[-1]] == m2[s[i]]):
                stack.pop(-1)
            elif s[i] in m1:
                stack.append(s[i])
                
            
        if len(stack) == 0:
            return True
        return False