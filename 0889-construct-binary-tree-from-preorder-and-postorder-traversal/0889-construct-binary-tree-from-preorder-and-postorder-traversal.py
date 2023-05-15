# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preInd = {v:i for i, v in enumerate(preorder)}
        def solve(l, r, postorder):
            if l == r: return None
            if r-l == 1: return TreeNode(postorder.pop())
            root = TreeNode(postorder.pop())
            i = preInd[postorder[-1]]
            root.right = solve(i, r, postorder)
            root.left = solve(l+1, i, postorder)
            return root
        
        return solve(0, len(preorder), postorder)
    