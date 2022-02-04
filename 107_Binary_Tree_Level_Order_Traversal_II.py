# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def levelOrderBottom(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root is None:
    #         return []
    #     self.get_level(res, root, 0)
    #     # reverse result
    #     res.reverse()
    #     return res
    #
    # def get_level(self, res, root, depth):
    #     if root is None:
    #         return
    #     if depth == len(res):
    #         res.append([])
    #     res[depth].append(root.val)
    #     self.get_level(res, root.left, depth + 1)
    #     self.get_level(res, root.right, depth + 1)
    def levelOrderBottom(self, root):
        if root is None:
            return []
        # use stack
        stack = [[root]]
        res = []
        while len(stack) > 0:
            top = stack.pop()
            res.insert(0, [t.val for t in top])
            temp = []
            for node in top:
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            if len(temp) > 0:
                stack.append(temp)
        return res