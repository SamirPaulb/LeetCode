# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def path(root,s ):
            if not root:
                return
            if root.left == None and root.right == None:
                ans.append(s+ str(root.val))
            if root.left:
                path(root.left, s = s + str(root.val) + "->")
            if root.right:
                path(root.right, s=  s + str(root.val) + "->")
        path(root, "")
        return ans