class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        for i in nums1:
            if i in nums2:
                a.append(i)
                nums2.remove(i)
        return a
    
    
    