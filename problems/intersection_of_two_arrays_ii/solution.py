class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l3 = []
        for val in nums1:
            if val in nums2:
                nums2.remove(val)
                l3.append(val)
        return l3

