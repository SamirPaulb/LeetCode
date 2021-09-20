# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = {}
        q = []
        if root == None: return 
        q.append([root, 0])
        while q:
            node = q.pop(0)
            v = node[0]  # the node
            h = node[1]  # Height of this node
            if h not in d: 
                d[h] = v.val
            if v.left: q.append([v.left, h+1])
            if v.right: q.append([v.right, h+1])
        mk = max(d.keys()) # mk = max value of key ==> Max height
        return d[mk]
            
            