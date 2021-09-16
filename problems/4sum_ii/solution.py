class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        myDict = {}
        count = 0
        for a in nums1:
            for b in nums2:
                if (a+b) in myDict:
                    myDict[a+b] += 1
                else:
                    myDict[a+b] = 1
        for c in nums3:
            for d in nums4:
                target = 0 - (c+d)
                if target in myDict:
                    count += myDict[target]
        return count