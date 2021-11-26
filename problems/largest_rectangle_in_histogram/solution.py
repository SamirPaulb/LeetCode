class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lb, rb, = [], []
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    lb.append(stack[-1] + 1)
                    stack.append(i)
                    break
            if not stack:
                stack.append(i)
                lb.append(0)
        
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    rb.append(stack[-1] - 1)
                    stack.append(i)
                    break
            if not stack:
                stack.append(i)
                rb.append(len(heights) - 1)
        rb = rb[::-1]
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (abs(rb[i] - lb[i]) + 1))
        
        return ans
            
            
            
            
            
            
            
            
            
            