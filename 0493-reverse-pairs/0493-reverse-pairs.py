class Solution:
    def __init__(self):
        self.res = 0
    
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            left = self.mergeSort(nums[:mid])
            right = self.mergeSort(nums[mid:])
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2*right[j]:
                    j += 1
                self.res += j
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        return nums
            
    
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.res
        