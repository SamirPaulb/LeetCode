class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = None
        prevDiff = float("inf")
        for i, ch in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = ch + nums[l] + nums[r]
                if abs(target - threeSum) < prevDiff: 
                    prevDiff = abs(target - threeSum)
                    ans = threeSum
                    
                if threeSum < target: l += 1
                elif threeSum > target: r -= 1
                else: return threeSum
                        
        return ans