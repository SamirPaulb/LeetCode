class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two points
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(min(height[left], height[right]) * (right - left), result)
            if height[left] > height[right]:
                # remove right
                right -= 1
            else:
                # remove left
                left += 1
        return result
