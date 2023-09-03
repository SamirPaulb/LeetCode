class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lb = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: lb[i] = stack[-1] + 1
            stack.append(i)
        
        rb = [n-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: rb[i] = stack[-1] - 1
            stack.append(i)
        
        res = 0
        for i in range(n):
            res = max(res, heights[i] * (rb[i] - lb[i] + 1))
        
        return res