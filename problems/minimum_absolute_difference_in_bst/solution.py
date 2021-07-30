# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        a = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            a.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        ans = a[1] - a[0]
        for i in range(1,len(a)-1):
            ans = min(ans, a[i+1] - a[i])
        return ans