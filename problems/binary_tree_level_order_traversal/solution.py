# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        res = []
        q = [root]
        while q:
            tmpArr = []
            for i in range(len(q)):
                tmpNode = q.pop(0)
                tmpArr.append(tmpNode.val)
                if tmpNode.left: q.append(tmpNode.left)
                if tmpNode.right: q.append(tmpNode.right)
            res.append(tmpArr)
        
        return res