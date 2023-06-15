class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        mid = (n1 + n2) // 2
        prev = cur = 0
        i = j = 0
        k = 0
        while k <= mid:
            if i < n1 and j < n2:
                if nums1[i] <= nums2[j]:
                    val = nums1[i]
                    i += 1
                else:
                    val = nums2[j]
                    j += 1
            elif j < n2:
                val = nums2[j]
                j += 1
            else:
                val = nums1[i]
                i += 1
            k += 1
            prev = cur
            cur = val
        
        return cur if (n1+n2)%2 else (prev+cur)/2