class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack:
                stack.append(n)
                continue
            elif len(stack)%2 and stack[-1] <= n:  # Odd index
                stack.pop()
            elif not len(stack)%2 and stack[-1] >= n:  # even index
                stack.pop()
            stack.append(n)
                
        if not len(stack)%2:
            stack.pop()

        print(stack)
        res = 0
        for i in range(1, len(stack)+1):
            if i%2:
                res += stack[i-1]
            else:
                res -= stack[i-1]
        
        return res