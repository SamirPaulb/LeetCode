# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.longestConsecutive_helper(root, -10000, 1)

    def longestConsecutive_helper(self, root, previous, curr):
        # Top down recursion
        if root is None:
            return 0
        if root.val - 1 == previous:
            curr += 1
        else:
            curr = 1
        l_res = self.longestConsecutive_helper(root.left, root.val, curr)
        r_res = self.longestConsecutive_helper(root.right, root.val, curr)
        return max(curr, l_res, r_res)

    # def __init__(self):
    #     self.max_length = 0

    # def longestConsecutive(self, root):
    #     self.longestConsecutive_helper(root)
    #     return self.max_length

    # def longestConsecutive_helper(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # Bottom up
    #     if root is None:
    #         return 0
    #     l_res = self.longestConsecutive_helper(root.left) + 1
    #     r_res = self.longestConsecutive_helper(root.right) + 1
    #     if root.left is not None and root.val + 1 != root.left.val:
    #         l_res = 1
    #     if root.right is not None and root.val + 1 != root.right.val:
    #         r_res = 1
    #     length = max(l_res, r_res)
    #     self.max_length = max(self.max_length, length)
    #     return length
