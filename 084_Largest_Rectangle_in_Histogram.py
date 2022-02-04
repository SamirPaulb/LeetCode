class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # https://leetcode.com/discuss/70983/4ms-java-solution-using-o-n-stack-space-o-n-time
        largest_rectangle = 0
        ls = len(heights)
        # heights[stack[top]] > heights[pos] > heights[stack[top - 1]]
        # keep the increase order
        stack = [-1]
        top, pos = 0, 0
        for pos in range(ls):
            while top > 0 and heights[stack[top]] > heights[pos]:
                largest_rectangle = max(largest_rectangle, heights[stack[top]] * (pos - stack[top - 1] - 1))
                top -= 1
                stack.pop()
            stack.append(pos)
            top += 1
        while top > 0:
            largest_rectangle = max(largest_rectangle, heights[stack[top]] * (ls - stack[top - 1] - 1))
            top -= 1
        return largest_rectangle


if __name__ == "__main__":
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
