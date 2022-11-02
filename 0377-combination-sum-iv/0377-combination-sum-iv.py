class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(nums, target):
            if target < 0: return 0
            if target == 0: return 1
            if target in memo: return memo[target]
            ans = 0
            for i in range(len(nums)):
                ans += solve(nums, target - nums[i])
            memo[target] = ans
            return ans
        
        return solve(nums, target)