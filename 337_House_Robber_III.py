# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     dic = {}
    #     return self.rob_helper(root, dic)
    #
    # def rob_helper(self, root, dic):
    #     # recursion with hash map
    #     if root is None:
    #         return 0
    #     if root in dic:
    #         return dic[root]
    #     res = 0
    #     if root.left is not None:
    #         res += self.rob_helper(root.left.left, dic) + self.rob_helper(root.left.right, dic)
    #     if root.right is not None:
    #         res += self.rob_helper(root.right.left, dic) + self.rob_helper(root.right.right, dic)
    #     res =  max(res + root.val, self.rob_helper(root.left, dic) + self.rob_helper(root.right, dic))
    #     dic[root] = res
    #     return res

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # res[0] means skip curr, res[1] means get curr
        res = self.rob_helper(root)
        return max(res[0], res[1])

    def rob_helper(self, root):
        if root is None:
            return [0, 0]
        left = self.rob_helper(root.left)
        right = self.rob_helper(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res