class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums) 
        def hr1(arr):
            if len(arr) < 3: return max(arr)
            for i in range(2, len(arr)):
                if i-3 >= 0:
                    arr[i] += max(arr[i-2], arr[i-3])
                else:
                    arr[i] += arr[i-2]
            return max(arr[-1], arr[-2])
        
        return max(hr1(nums[:-1]), hr1(nums[1:]))