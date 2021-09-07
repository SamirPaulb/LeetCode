class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                ans.append(nums2[i])
                nums1.remove(nums2[i])
        return list(set(ans))