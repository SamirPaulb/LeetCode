# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def findSecondMinimumValue(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # Brute force
    #     values = set()
    #     self.dfs(root, values)
    #     ans, min_value = float('inf'), root.val
    #     for n in values:
    #         if min_value < n and n < ans:
    #             ans = n
    #     return ans if ans < float('inf') else -1

    # def dfs(self, root, values):
    #     if not root:
    #         return
    #     values.add(root.val)
    #     self.dfs(root.left, values)
    #     self.dfs(root.right, values)

    def findSecondMinimumValue(self, root):
        if not root:
            return -1
        ans = float('inf')
        min_val = root.val
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if min_val < curr.val < ans:
                ans = curr.val
            elif curr.val == min_val:
                stack.append(curr.left)
                stack.append(curr.right)
        return ans if ans < float('inf') else -1
