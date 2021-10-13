# First Solve --> 84.Largest Rectangle in Histogram
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        arr = [int(i) for i in matrix[0]] 
        ans = self.largestRectangleArea(arr)
        for i in range(1, len(matrix)):
            for j in range(len(arr)):
                if matrix[i][j] == "1":
                    arr[j] += 1
                else:
                    arr[j] = 0
            ans = max(ans, self.largestRectangleArea(arr))
        #print(arr)
        return ans
            
    # 84. Largest Rectangle in Histogram   
    # https://leetcode.com/problems/largest-rectangle-in-histogram/
    def largestRectangleArea(self, heights):
        # Finding Left Boundary
        stack = []
        lb = []  # Left Boundary
        for i in range(len(heights)):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    lb.append(stack[-1] + 1)
                    stack.append(i)
                    break
            if len(stack) == 0:
                stack.append(i)
                lb.append(0)
        # Finding Right Boundary
        stack = []
        rb = []
        for i in range(len(heights)-1, -1, -1):
            while stack:
                if heights[stack[-1]] >= heights[i]:
                    stack.pop()
                else:
                    rb.append(stack[-1] - 1)
                    stack.append(i)
                    break
            if len(stack) == 0:
                stack.append(i)
                rb.append(len(heights) - 1)
        rb = rb[::-1]
        
        maxArea = 0
        for i in range(len(heights)):
            weight = abs(lb[i] - rb[i]) + 1
            height = heights[i]
            maxArea = max(maxArea, weight * height)
        
        return maxArea
                