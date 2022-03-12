class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in range(len(nums1)):
            if i+res < len(nums2):
                for j in range(i+res, len(nums2)):
                    if nums2[j] >= nums1[i]:
                        res = j - i
                    else:
                        break
                        
        return res