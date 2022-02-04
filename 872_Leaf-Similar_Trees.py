# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        leaf1 = []
        leaf2 = []
        self.dfs(root1, leaf1)
        self.dfs(root2, leaf2)
        if leaf1 == leaf2:
            return True
        return False

    def dfs(self, node, leavels):
        if not node:
            return
        if not node.left and not node.right:
            leavels.append(node.val)
        self.dfs(node.left, leavels)
        self.dfs(node.right, leavels)
