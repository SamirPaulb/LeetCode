# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def recoverTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: void Do not return anything, modify root in-place instead.
    #     """
    #     # https://discuss.leetcode.com/topic/9305/detail-explain-about-how-morris-traversal-finds-two-incorrect-pointer/2
    #     pre = first = second = None
    #     while root is not None:
    #         if root.left is not None:
    #             temp = root.left
    #             while temp.right is not None and temp.right != root:
    #                 temp = temp.right
    #             if temp.right is not None:
    #                 if pre is not None and pre.val > root.val:
    #                     if first is None:
    #                         first = pre
    #                     second = root
    #                 pre = root
    #                 temp.right = None
    #                 root = root.right
    #             else:
    #                 temp.right = root
    #                 root = root.left
    #         else:
    #             if pre is not None and pre.val > root.val:
    #                 if first is None:
    #                     first = pre
    #                 second = root
    #             pre = root
    #             root = root.right
    #     # only two elements are swapped
    #     if first is not None and second is not None:
    #         first.val, second.val = second.val, first.val


    # https://discuss.leetcode.com/topic/3988/no-fancy-algorithm-just-simple-and-powerful-in-order-traversal/2
    def __init__(self):
        self.first = self.second = None
        self.pre = TreeNode(-sys.maxint - 1)


    def recoverTree(self, root):
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if self.pre.val >= root.val:
            if self.first is None:
                self.first = self.pre
            if self.first is not None:
                self.second = root
        self.pre = root
        self.traverse(root.right)



