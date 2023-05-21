# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inIndex = {v:i for i, v in enumerate(inorder)}
        self.i = 0
        def solve(l, r):
            if l > r: return None
            v = preorder[self.i]
            self.i += 1
            root = TreeNode(v)
            i = inIndex[v]
            root.left = solve(l, i-1)
            root.right = solve(i+1, r)
            return root
        
        return solve(0, len(inorder)-1)