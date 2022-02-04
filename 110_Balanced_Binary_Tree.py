# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Bottom-up recursion with sentinel -1
        if root is None:
            return True
        if self.getDepth(root) < 0:
            return False
        return True
    
    def getDepth(self, node):
        if node is None:
            return 1
        ld = self.getDepth(node.left)
        if ld < 0:
            return -1
        rd = self.getDepth(node.right)
        if rd < 0:
            return -1
        elif abs(ld - rd) > 1:
            return -1
        else:
            return max(ld, rd) + 1
    

    # https://discuss.leetcode.com/topic/7798/the-bottom-up-o-n-solution-would-be-better
    # def isBalanced(self, root):
    #     # Top-down recursion
    #     if root is None:
    #         return True
    #     left = self.depth(root.left)
    #     right = self.depth(root.right)
    #     return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # def depth(self, root):
    #     if root is None:
    #         return 0
    #     return max(self.depth(root.left), self.depth(root.right)) + 1
        



