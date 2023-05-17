# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colDict = {}
        def solve(root, c, l):
            if not root: return 
            if c not in colDict:
                colDict[c] = [(l, root.val)]
            else:
                colDict[c].append((l, root.val))
            solve(root.left, c-1, l+1)
            solve(root.right, c+1, l+1)
        
        solve(root, 0, 0)
        keys = sorted(list(colDict.keys()))
        # print(colDict)
        res = []
        for key in keys:
            tmp = []
            for l, v in sorted(colDict[key]):
                tmp.append(v)
            res.append(tmp)
        return res