# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        mv = max(nums) # Max Value
        mi = nums.index(mv) # Index of Max Value
        root = TreeNode(mv)
        root.left = self.constructMaximumBinaryTree(nums[:mi])
        root.right = self.constructMaximumBinaryTree(nums[mi+1:])
        return root