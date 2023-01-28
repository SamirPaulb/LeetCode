class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while open_stack and star_stack:
            if open_stack[-1] > star_stack[-1]:
                return False
            open_stack.pop()
            star_stack.pop()
            
        return len(open_stack) == 0