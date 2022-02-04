# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root is None:
    #         return True
    #     order_list = self.getOrder(root)
    #     length = len(order_list)
    #     for i in range(length):
    #         if (i + 1) < length and order_list[i + 1] <= order_list[i]:
    #             return False
    #     return True
    #
    # def getOrder(self, node):
    #     result = []
    #     if node is None:
    #         return result
    #     result.extend(self.getOrder(node.left))
    #     result.append(node.val)
    #     result.extend(self.getOrder(node.right))
    #     return result

    def isValidBST(self, root):
        return self.isVaild_helper(root, -sys.maxint - 1, sys.maxint)

    def isVaild_helper(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isVaild_helper(root.left, minVal, root.val) and self.isVaild_helper(root.right, root.val, maxVal)
