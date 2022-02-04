# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.get_trees(1, n)

    def get_trees(self, start, end):
        # recursive solve this problem
        res = []
        if start > end:
            res.append(None)
            return res
        for i in range(start, end + 1):
            lefts = self.get_trees(start, i - 1)
            rights = self.get_trees(i + 1, end)
            for j in range(len(lefts)):
                for k in range(len(rights)):
                    # root point
                    root = TreeNode(i)
                    root.left = lefts[j]
                    root.right = rights[k]
                    res.append(root)
        return res


