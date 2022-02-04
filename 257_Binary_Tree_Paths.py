# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        paths = []
        self.get_path(paths, [], root)
        res = ['->'.join(p) for p in paths ]
        return res

    def get_path(self, result, path, node):
        if node.left is None and node.right is None:
            result.append(path + [str(node.val)])
            return
        path = path + [str(node.val)]
        if node.left is not None:
            self.get_path(result, path, node.left)
        if node.right is not None:
            self.get_path(result, path, node.right)