class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
            if stack and stack[-1][0] == i:
                stack.append((i, stack[-1][1] + 1))
            else:
                stack.append((i, 1))
        
        if stack and stack[-1][1] == k:
            for _ in range(k):
                stack.pop()
        
        return "".join(c for c, i in stack)