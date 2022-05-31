# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = {}
        def solve(root, d, l):
            if not root: return
            
            if d not in self.dic:
                self.dic[d] = [(l, root.val)]
            else:
                self.dic[d].append((l, root.val))
                
            solve(root.left, d-1, l+1)
            solve(root.right, d+1, l+1)
        
        solve(root, 0, 0)
        keys = sorted(list(self.dic.keys()))
        
        res = []
        for key in keys:
            values = self.dic[key]
            values.sort()
            #print(values)
            res.append([r[1] for r in values])
            
        return res