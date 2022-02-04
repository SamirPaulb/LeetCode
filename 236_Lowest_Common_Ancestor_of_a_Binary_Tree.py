# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     self.ans = None

    #     def lowestCommonAncestorHelper(node):
    #         if not node:
    #             return False
    #         left = lowestCommonAncestorHelper(node.left)
    #         right = lowestCommonAncestorHelper(node.right)
    #         mid = node == p or node == q
    #         if mid + left + right >= 2:
    #             self.ans = node
    #         return mid or left or right
    #     lowestCommonAncestorHelper(root)
    #     return self.ans

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Stack for tree traversal
        stack = [root]
        # Dictionary for parent pointers
        parent = {root: None}
        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
