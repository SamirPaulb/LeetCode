class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        # if start < mid, then left part is sorted
        # if mid < end, then right part is sorted
        def get(start, end):
          if start > end:
            return -1
          mid = (start + end) / 2
          if nums[mid] == target:
            return mid
          elif nums[mid] >= nums[start]: # First half is sorted
            if target >= nums[start] and target < nums[mid]:
              return get(start, mid - 1)
            else:
              return get(mid + 1, end)
          elif nums[mid] <= nums[end]: # Second half is sorted
            if target > nums[mid] and target <= nums[end]:
              return get(mid + 1, end)
            else:
              return get(start, mid - 1)
        return get(0, len(nums) - 1)