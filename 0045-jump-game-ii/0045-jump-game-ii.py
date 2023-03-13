class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = maxreachable = res = 0
        while r < len(nums) - 1:
            for i in range(l, r+1):
                maxreachable = max(maxreachable, i + nums[i])
            l = r+1
            r = maxreachable
            res += 1
            
        return res