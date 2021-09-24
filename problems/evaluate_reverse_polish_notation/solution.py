class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > 1:
            res = 2**31
            if tokens[i] == "+":  
                a = int(tokens[i-2])
                b = int(tokens[i-1])
                res = a + b
            elif tokens[i] == "-":
                a = int(tokens[i-2])
                b = int(tokens[i-1])
                res = a - b
            elif tokens[i] == "*":
                a = int(tokens[i-2])
                b = int(tokens[i-1])
                res = a * b
            elif tokens[i] == "/":
                a = int(tokens[i-2])
                b = int(tokens[i-1])
                res = int(a / b)
            if res != 2**31:
                tokens.pop(i)
                tokens.pop(i-1)
                tokens[i-2] = res
                i = i-2
            i += 1
        return int(tokens.pop())