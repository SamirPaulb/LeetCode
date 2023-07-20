class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num * 10 + int(s[i])
                    i += 1
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                    
                i -= 1
            elif s[i] != ' ':
                sign = s[i]
            i += 1
                
        return sum(stack)
                    