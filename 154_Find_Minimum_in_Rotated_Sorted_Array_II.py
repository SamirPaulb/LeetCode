class Solution(object):
    # def findMin(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     return self.get_min(nums, 0, len(nums) - 1)

    # def get_min(self, nums, start, end):
    #     mid = (start + end) / 2
    #     if start == end:
    #         # one element
    #         return nums[start]
    #     if mid == start or mid == end:
    #         # two element
    #         return min(nums[start], nums[end])
    #     if nums[mid] < nums[end]:
    #         # right side sorted
    #         if nums[mid] > nums[start]:
    #             # not rotated
    #             return nums[start]
    #         return self.get_min(nums, start, mid)
    #     elif nums[mid] > nums[end]:
    #         # left side sorted
    #         return self.get_min(nums, mid, end)
    #     else:
    #         # cannot judge which direction is sorted
    #         return min(self.get_min(nums, start, mid), self.get_min(nums, mid, end))

    # def findMin(self, nums):
    #     start, end = 0, len(nums) - 1
    #     while start < end:
    #         mid = (start + end) / 2
    #         if nums[mid] > nums[end]:
    #             start = mid + 1
    #         elif nums[mid] < nums[end]:
    #             end = mid
    #         else:
    #             end -= 1
    #     return nums[start]


    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            mid = (l + r) / 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                # nums[l] = nums[r] = nums[mid]
                l += 1
        return nums[l]


