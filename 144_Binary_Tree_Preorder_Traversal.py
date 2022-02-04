# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def __init__(self):
    #     self.result = []
    #
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root is None:
    #         return []
    #     self.preorderTraversalHelper(root)
    #     return self.result
    #
    # def preorderTraversalHelper(self, node):
    #     if node is None:
    #         return
    #     self.result.append(node.val)
    #     self.preorderTraversalHelper(node.left)
    #     self.preorderTraversalHelper(node.right)

    def preorderTraversal(self, root):
        # stack
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res

