# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        # bfs with queue
        queue = [(root, root.val)]
        while len(queue) > 0:
            curr, curr_value = queue.pop(0)
            if curr.left is None and curr.right is None:
                res += curr_value
                continue
            if curr.left:
                queue.append((curr.left, curr_value * 10 + curr.left.val))
            if curr.right:
                queue.append((curr.right, curr_value * 10 + curr.right.val))
        return res
