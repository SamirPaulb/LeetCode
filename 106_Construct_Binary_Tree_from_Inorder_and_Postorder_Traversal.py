# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        inOrderMap = {inorder[i]: i for i in range(n)}
        return self.buildTreeUtil(inorder, postorder, inOrderMap, 0, n - 1, 0, n - 1)

    def buildTreeUtil(self, inorder, postorder, inOrderMap, pStart, pEnd, iStart, iEnd):
        if pStart > pEnd or iStart > iEnd:
            return None

        root = TreeNode(postorder[pEnd])
        rootIdx = inOrderMap[root.val]
        root.left = self.buildTreeUtil(inorder, postorder, inOrderMap, pStart, pStart + rootIdx - iStart - 1, iStart,
                                       rootIdx - 1)
        root.right = self.buildTreeUtil(inorder, postorder, inOrderMap, pStart + rootIdx - iStart, pEnd - 1, rootIdx + 1,
                                        iEnd)
        return root

