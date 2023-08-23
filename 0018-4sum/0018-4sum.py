class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                l, r = j+1, n-1
                s1 = nums[i] + nums[j]
                while l < r:
                    s2 = nums[l] + nums[r]
                    if s1 + s2 < target:
                        l += 1
                    elif s1 + s2 > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        
        return res