# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        sumt = 0
        def tilt(root):
            nonlocal sumt
            if root == None:
                return 0
            lt = tilt(root.left)
            rt = tilt(root.right)
            sumt += abs(lt-rt)
            ts = root.val + lt + rt
            return ts
        tilt(root)
        return sumt