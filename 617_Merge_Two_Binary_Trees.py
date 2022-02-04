# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    # def mergeTrees(self, t1, t2):
    #     if t1 is None:
    #         return t2
    #     stack = [(t1, t2)]
    #     while len(stack) != 0:
    #         n1, n2 = stack.pop()
    #         if n1 is None or n2 is None:
    #             continue
    #         n1.val += n2.val
    #         if n1.left is None:
    #             n1.left = n2.left
    #         else:
    #             stack.insert(0, (n1.left, n2.left))
    #         if n1.right is None:
    #             n1.right = n2.right
    #         else:
    #             stack.insert(0, (n1.right, n2.right))
    #     return t1
