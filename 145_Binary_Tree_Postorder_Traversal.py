# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     # Recursion
    #     if root is None:
    #         return []
    #     res = []
    #     self.postorderHelp(root, res)
    #     return res
    #
    # def postorderHelp(self, node, stack):
    #     if node is None:
    #         return
    #     self.postorderHelp(node.left, stack)
    #     self.postorderHelp(node.right, stack)
    #     stack.append(node.val)

    # def postorderTraversal(self, root):
    #     # Stack
    #     if root is None:
    #         return []
    #     res = []
    #     stack = [root]
    #     while len(stack) > 0:
    #         curr = stack.pop()
    #         res.insert(0, curr.val)
    #         if curr.left is not None:
    #             stack.append(curr.left)
    #         if curr.right is not None:
    #             stack.append(curr.right)
    #     return res

    def postorderTraversal(self, root):
        if root is None:
            return []
        res = []; stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            stack.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res
