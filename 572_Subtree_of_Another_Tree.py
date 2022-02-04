# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # https://leetcode.com/problems/subtree-of-another-tree/solution/
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_res = self.preorder(s, True)
        t_res = self.preorder(t, True)
        return t_res in s_res
    
    def preorder(self, root, isLeft):
        if root is None:
            if isLeft:
                return "lnull"
            else:
                return "rnull"
        return "#" + str(root.val) + " " + self.preorder(root.left, True) + " " + self.preorder(root.right, False)

    # def isSubtree(self, s, t):
    #     return self.traverse(s, t)
    
    # def equals(self, x, y):
    #     if x is None and y is None:
    #         return True
    #     if x is None or y is None:
    #         return False
    #     return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)
    
    # def traverse(self, s, t):
    #     return s is not None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))
