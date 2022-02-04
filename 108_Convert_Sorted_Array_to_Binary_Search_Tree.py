# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     # Recursion with slicing
    #     if not nums:
    #         return None
    #     mid = len(nums) / 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.sortedArrayToBST(nums[:mid])
    #     root.right = self.sortedArrayToBST(nums[mid + 1:])
    #     return root

    def sortedArrayToBST(self, nums):
        # Recursion with index
        return self.getHelper(nums, 0, len(nums) - 1)

    def getHelper(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        node.left = self.getHelper(nums, start, mid - 1)
        node.right = self.getHelper(nums, mid + 1, end)
        return node