# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        a = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            a.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        a_ = list(set(a))
        ans = []
        m = []
        for i in range(len(a_)):
            ans.append([a_[i], a.count(a_[i])])
            m.append(a.count(a_[i]))
        mi = max(m)
        res = []
        for i in range(len(ans)):
            if ans[i][1] == mi:
                res.append(ans[i][0])
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        