# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # O (n^2) and O(n)
        if nums is None or len(nums) == 0:
            return None
        max_index, max_value = 0, 0
        for i, value in enumerate(nums):
            if value >= max_value:
                max_value = value
                max_index = i
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

    # def constructMaximumBinaryTree(self, nums):
    #     # https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C++-O(N)-solution
    #     stack = []
    #     for value in nums:
    #         curr = TreeNode(value)
    #         while len(stack) != 0 and stack[-1].val < value:
    #             curr.left = stack[-1]
    #             stack.pop()
    #         if (len(stack) != 0):
    #             stack[-1].right = curr
    #         stack.append(curr)
    #     return stack[0]
