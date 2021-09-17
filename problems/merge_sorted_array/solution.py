class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            nums1.pop()
        i = 0
        while i < len(nums1):
            if len(nums2) != 0 and nums1[i] > nums2[0]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
            if len(nums2) != 0 and nums1[i] > nums2[0]:
                i -= 1
            i += 1
        if nums2:
            nums1 += nums2
        
# Time Complexity = O(n)