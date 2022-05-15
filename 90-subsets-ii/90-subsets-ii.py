class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def solve(i, path):
            if i >= len(nums):
                res.append(path)
                return

            solve(i+1, path + [nums[i]])
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            solve(i+1, path)
        
        solve(0, [])
        return res