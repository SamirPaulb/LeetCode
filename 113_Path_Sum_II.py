# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        if sum == root.val and root.left is None and root.right is None:
            return [[root.val]]
        # left side
        left_res = self.pathSum(root.left, sum - root.val)
        # right side
        right_res = self.pathSum(root.right, sum - root.val)
        # add current prefix
        for t in left_res + right_res:
            res.append([root.val] + t)
        return res
