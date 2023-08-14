#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        order = {'+':0, '-':0, '*':1, '/':1, '^':2}
        res = ''
        stack = []
        for i in exp:
            if i not in '+-*/^()':
                res += i
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while stack:
                    top = stack.pop()
                    if top == '(':
                        break
                    res += top
            else:
                while stack and stack[-1] in order and order[i] <= order[stack[-1]]:
                    res += stack.pop()
                stack.append(i)
        
        res += ''.join(stack)
        return res




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends