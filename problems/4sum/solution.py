class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            tar = target - nums[i]
            # 3 Sum approach
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    threeSum = nums[j] + nums[l] + nums[r]
                    if threeSum < tar: l += 1
                    elif threeSum > tar: r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r: l += 1
                            
        return res
    