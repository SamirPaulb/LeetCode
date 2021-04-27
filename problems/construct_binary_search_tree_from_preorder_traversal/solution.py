class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for index in range(1, len(preorder)):
            new_node = TreeNode(preorder[index])
            if new_node.val < stack[-1].val:
                stack[-1].left = new_node
            else:
                parent = None
                while stack and new_node.val > stack[-1].val:
                    parent = stack.pop()
                parent.right = new_node
            stack.append(new_node)
        return root
        