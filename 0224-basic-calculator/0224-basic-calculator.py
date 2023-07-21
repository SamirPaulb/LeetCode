class Solution:
    def calculate(self, s: str) -> int:
        stack = []; sign = 1
        i = 0
        while i < len(s): 
            if s[i] == ' ': 
                i += 1
                continue
            elif s[i] == '+': sign = 1
            elif s[i] == '-': sign = -1
            elif s[i] == '(': 
                stack.append(sign)
                stack.append(s[i])
                sign = 1
            elif s[i].isdigit(): 
                num = 0; j = i
                while j < len(s) and s[j].isdigit():
                    num = num * 10 + int(s[j])
                    j += 1
                i = j if i < j else j+1
                stack.append(sign * num)
                i -= 1
            else: # ch == ')'
                tmp = 0
                while stack:
                    top = stack.pop()
                    if top == '(': break
                    tmp += top
                sign = stack.pop()
                stack.append(sign * tmp)
            i += 1
            # print(stack)
        return sum(stack)