class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = list(preorder.split(','))
        if preorder[0] == '#':
            if len(preorder) == 1: return True
            return False
        
        stack = []
        for i, ch in enumerate(preorder):
            if ch == '#':
                if not stack: return False
                stack[-1] -= 1
                while stack and stack[-1] <= 0:
                    stack.pop()
                    if stack: stack[-1] -= 1
            else:
                if i != 0 and not stack: return False
                stack.append(2)
                
        # print(stack)
        return True if not stack else False 