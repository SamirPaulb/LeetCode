# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if root == None:
                return 0
            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        def findNode(root, curDepth, depth):
            if root != None:
                if curDepth == depth:
                    self.res += root.val
                findNode(root.left, curDepth + 1, depth)
                findNode(root.right, curDepth + 1, depth)
        
        depth = maxDepth(root)
        print(depth)
        findNode(root, 1, depth)
        return self.res