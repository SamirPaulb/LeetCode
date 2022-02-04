# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # stack
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        current = root
        stack = [root]
        while stack:
            node = stack.pop()
            self.appendNode(stack, node.right)
            self.appendNode(stack, node.left)
            if current != node:
                current.right = node
                current.left = None
                current = node

    def appendNode(self, stack, node):
        if node:
            stack.append(node)

    # recursive
    # https://discuss.leetcode.com/topic/11444/my-short-post-order-traversal-java-solution-for-share/2
    # def __init__(self):
    #     self.prev = None
    #
    # def flatten(self, root):
    #     if root is None:
    #         return
    #     self.flatten(root.right)
    #     self.flatten(root.left)
    #     root.right = self.prev
    #     root.left = None
    #     self.prev = root





