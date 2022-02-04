class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        pos1 = pos2 = 0
        while pos1 < len(nums1) and pos2 < len(nums2):
            if nums1[pos1] == nums2[pos2]:
                res.append(nums1[pos1])
                pos1 += 1
                pos2 += 1
            elif nums1[pos1] < nums2[pos2]:
                pos1 += 1
            else:
                pos2 += 1
        return res
