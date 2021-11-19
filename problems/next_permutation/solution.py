# https://www.youtube.com/watch?v=6qXO72FkqwM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        sp = -1 # Swap Point
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                sp = i
        # Checking if sp == -1; eg. nums = [5, 4, 3, 2, 1]; => NO next greater permutation exit => return [1, 2, 3, 4, 5]
        if sp == -1:
            # Sort the whole array
            l, r = 0, n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
        # Checking for nums = [1, 2, 3, 5, 4, 2]; sp = 3; but we have to swap b/t 3 and 4
        leftSwapInd = sp - 1
        rightSwapInd = sp
        for i in range(sp, n):
            if nums[leftSwapInd] < nums[i]:
                rightSwapInd = i
        # Swap b/t 3 and 4
        nums[leftSwapInd], nums[rightSwapInd] = nums[rightSwapInd], nums[leftSwapInd]
        # Now nums = [1, 2, 4, 5, 3, 2]; but ans should be [1, 2, 4, 2, 3, 5]
        # So sort right side elements of sp in increasing order
        l, r = sp, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums