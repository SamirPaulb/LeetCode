# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dct = {}
        def solve(root, d, l):
            if not root: return 
            if d not in dct: dct[d] = [(l, root.val)]
            else: dct[d].append((l, root.val))
            solve(root.left, d-1, l+1)
            solve(root.right, d+1, l+1)
        
        solve(root, 0, 0)
        res = []
        for key in sorted(list(dct.keys())):
            res.append([v for l, v in sorted(dct[key])])
        return res