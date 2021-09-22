class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        for i in s:
            if len(stack) == 0 and (i == ")" or i == "]" or i == "}"):
                return False
            
            elif len(stack) == 0:
                stack.append(i)
                
            else:
                if (stack[-1] == "(" and i == ")") or (stack[-1] == "{" and i == "}") or (stack[-1] == "[" and i == "]"):
                    stack.pop()
                else:
                    stack.append(i)
        print(stack)
        return len(stack) == 0
                
                