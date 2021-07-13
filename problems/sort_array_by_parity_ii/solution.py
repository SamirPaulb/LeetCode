class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = 0
        o = 1
        while o<len(nums) and e<len(nums):
            if nums[e] % 2 == 0:
                e += 2
            else:
                if nums[o] %2 != 0:
                    o += 2
                else:
                    nums[o], nums[e] = nums[e], nums[o]
                    o += 2
                    e += 2
        return nums