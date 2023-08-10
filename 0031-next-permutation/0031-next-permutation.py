class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = -1     
        for r in range(len(nums)-1, 0, -1):
            if nums[r-1] < nums[r]:
                l = r - 1
                break
        # print(l, r)
        if l == -1: 
            nums.sort()
            return nums

        for nr in range(r+1, len(nums)):
            if nums[l] < nums[nr] < nums[r]:
                r = nr
        
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, len(nums)
        nums[l:r] = sorted(nums[l:r])

        return nums