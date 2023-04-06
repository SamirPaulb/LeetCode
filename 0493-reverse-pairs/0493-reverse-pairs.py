class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.res = 0
        def mergesort(nums):
            if not nums or len(nums) == 1: return nums
            m = len(nums)//2
            left = mergesort(nums[:m])
            right = mergesort(nums[m:])
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2*right[j]:
                    j += 1
                self.res += j
            
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
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
        
        mergesort(nums)
        return self.res