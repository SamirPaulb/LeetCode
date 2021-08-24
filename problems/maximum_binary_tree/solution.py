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
            if len(nums) == 0:
                return root
            a = nums.index(root.val)
            if len(nums[:a]) != 0:
                root.left = TreeNode(max(nums[:a]))
            if len(nums[a+1:]) != 0:
                root.right = TreeNode(max(nums[a+1:]))
            tree(root.left, nums[:a])
            tree(root.right, nums[a+1:])
            
        tree(root, nums)
        return a