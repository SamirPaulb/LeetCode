class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 2**31
        ans = 0
        nums.sort()
        for i, ch in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                threeSum = ch + nums[l] + nums[r]
                if diff > abs(target - threeSum):
                    diff = abs(target - threeSum)
                    ans = threeSum
                if target < threeSum: r -= 1
                elif target > threeSum: l += 1
                else:
                    return threeSum
                    
        return ans