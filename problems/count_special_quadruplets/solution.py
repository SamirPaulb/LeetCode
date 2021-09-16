class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ans += 1
        
        return ans