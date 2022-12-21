class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        self.n = len(nums)
        self.res = 0
        
        def dfs(i, nums):
            if i > self.n: 
                self.res += 1
                return
            for j, ch in enumerate(nums):
                if ch % i == 0 or i % ch == 0:
                    dfs(i+1, nums[:j] + nums[j+1:])
        
        dfs(1, nums)
        return self.res