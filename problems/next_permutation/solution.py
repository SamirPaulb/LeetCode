class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # nums = [1,3,5,4,3,7,6,1]
        
        s1 = None
        for i in range(len(nums)-1, -0, -1):
            if nums[i] > nums[i-1]:
                s1 = i - 1
                break
        
        s2 = None
        if s1 != None:
            for i in range(len(nums)-1, s1, -1):
                if nums[i] > nums[s1]:
                    s2 = i
                    break
        
        if s1 != None and s2 != None:
            nums[s1], nums[s2] = nums[s2], nums[s1]
        # nums = [1,3,5,4,6,7,3,1]
        
        if s1 != None:
            l = s1 + 1; r = len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:
            l = 0; r = len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1