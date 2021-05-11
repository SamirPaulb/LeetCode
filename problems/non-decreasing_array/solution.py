
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        indices = []
        lo = 0
        hi = 0
        nums.append(float(inf))
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                indices.append((i, nums[i+1]))
                lo += 1
            if nums[i] >= nums[i+1]:
                indices.append((i, nums[i+1]))
                hi += 1
            if lo > 1 and hi > 1:
                break
        for index, value in indices:
            if nums[:index] + [value] + nums[index+1:-1] == sorted(nums[:index] + [value] + nums[index+1:-1]):
                return True
        return False if len(nums[:-1]) > 1 else True