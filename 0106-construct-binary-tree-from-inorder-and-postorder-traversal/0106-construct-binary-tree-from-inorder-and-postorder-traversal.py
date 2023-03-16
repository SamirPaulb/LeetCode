# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {ch:i for i, ch in enumerate(inorder)}
        self.pi = len(postorder)-1
        def solve(l, r):
            if l > r: return None
            root = TreeNode(postorder[self.pi])
            self.pi -= 1
            i = inorderIndex[root.val]
            root.right = solve(i+1, r)
            root.left = solve(l, i-1)
            return root
        
        return solve(0, len(inorder)-1)