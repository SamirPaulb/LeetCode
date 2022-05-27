class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums1Set = set(nums1)
        nextGreater = [-1] * len(nums2)
        indexDict = {}
        
        for i in range(len(nums2)-1, -1, -1):
            if nums2[i] in nums1Set:
                indexDict[nums2[i]] = i
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(nums2[i])
        
        res = []
        for num in nums1:
            res.append(nextGreater[indexDict[num]])
        
        return res