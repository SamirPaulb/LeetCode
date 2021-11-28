# https://www.youtube.com/watch?v=wuwE7g8VvgQ
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n):
            # Required number of elements = k - len(stack)
            rem = n - (i + 1)  # remaining elements in nums right side of i = len(nums[i:])
            while stack and stack[-1] > nums[i] and rem >= k - len(stack):
                stack.pop()
            
            if len(stack) < k: stack.append(nums[i])
        
        return stack