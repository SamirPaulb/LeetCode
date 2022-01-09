class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexDic = {}
        stack = []
        
        for i in range(len(nums2)-1, -1, -1):
            curr = nums2[i]
            while stack and stack[-1] <= curr:
                stack.pop()
            if not stack:
                indexDic[curr] = -1
            else:
                indexDic[curr] = stack[-1]
            stack.append(curr)
        
        res = []
        
        for num in nums1:
            res.append(indexDic[num])
        
        return res