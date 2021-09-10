# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(max(nums))
        a = root
        def tree(root, nums):
            i = nums.index(max(nums))
            if i>0: root.left = TreeNode(max(nums[:i]))
            if i < len(nums)-1: root.right = TreeNode(max(nums[i+1:]))
            if i>0: tree(root.left, nums[:i])
            if i < len(nums)-1: tree(root.right, nums[i+1:])
            return root
        tree(root, nums)
        return a