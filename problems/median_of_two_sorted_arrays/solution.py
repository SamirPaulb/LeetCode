class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        while i < len(nums1) and nums2:
            if nums2[0] < nums1[i]:
                nums1.insert(i, nums2.pop(0))
            i += 1
            
        if len(nums2) > 0:
            nums1 += nums2
        print(nums1)
        n = len(nums1)
        if len(nums1) % 2 == 0:
            return (nums1[n//2 - 1] + nums1[n//2]) / 2
        return nums1[n//2]
        