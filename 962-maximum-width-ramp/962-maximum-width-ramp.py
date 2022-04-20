class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        # Brute Force   # Time: O(N^2)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i] >= nums[j]:
                    res = max(res, i-j)
                    break
                    
        return res
        '''
        # Method 1   # Time: O(N log(N))
        # Keep a decreasing stack.For each number, binary search the first smaller number in the stack. When the number is smaller the the last, push it into the stack.
        stack = []
        res = 0
        for i in range(len(nums)-1, -1, -1):
            if not stack or nums[stack[-1][1]] < nums[i]:
                stack.append([nums[i], i])
            else:
                j = stack[bisect.bisect(stack, [nums[i], i])][1]
                res = max(res, j - i)
        
        return res