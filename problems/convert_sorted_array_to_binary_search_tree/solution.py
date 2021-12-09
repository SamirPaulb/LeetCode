# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binarySearch(nums, l, r):
            if l > r: return
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = binarySearch(nums, l, mid - 1)
            root.right = binarySearch(nums, mid + 1, r)
            return root
        
        return binarySearch(nums, 0, len(nums) - 1)