class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        nums += nums
        
        res = [-1] * len(nums)
        stack = []
        
        i = 0
        while i < len(nums):
            if stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
                i -= 1
            else:
                stack.append(i)
            i += 1
        
        return res[:n]