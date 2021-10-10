class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums2) == 0: return nums1
        for i in range(len(nums2)):
            nums1.pop()
        i = 0
        while i < len(nums1):
            if len(nums2) > 0 and nums2[0] <= nums1[i]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
            i += 1
        
        if len(nums2) > 0:
            nums1 += nums2
            
        