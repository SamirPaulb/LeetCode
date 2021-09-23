# https://www.youtube.com/watch?v=sDKpIO2HGq0

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # making a dictionary to check if i in dic as "in" function from dictionary takes O(1) time but "in" from list takes O(n) time
        dic = {}
        for i in nums1:
            dic[i] = 0
        for i in range(len(nums2)):
            if nums2[i] in dic:
                dic[nums2[i]] = i
        
        # Implementing solution of Next Greater problem for each element of a single list
        stack = []
        next_greater = [-1] * len(nums2)
        
        i = 0
        while i < len(nums2):
            if stack and nums2[stack[-1]] < nums2[i]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()
                i -= 1
            else:
                stack.append(i)
            i += 1
        
        # Now checking values from dictionary and appending to result array
        res = []
        for i in dic:
            res.append(next_greater[dic[i]]) # as index of next_greater and nums2 are same
        return res