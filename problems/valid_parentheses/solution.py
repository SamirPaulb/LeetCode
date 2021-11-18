class Solution:
    def isValid(self, s: str) -> bool:
        dOpen = {
            "(" : 1,
            "{" : 2,
            "[" : 3
        }
        dClose = {
            ")" : -1,
            "}" : -2,
            "]" : -3
        }
        
        stack = []
        for i in s:
            if len(stack) != 0 and stack[-1] in dOpen and i in dClose and dOpen[stack[-1]] + dClose[i] == 0:
                stack.pop()
            else: stack.append(i)
            
        return len(stack) == 0
        