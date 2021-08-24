# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            newNode = TreeNode(i)
            if newNode.val < stack[-1].val:
                stack[-1].left = newNode
            else:
                while stack and newNode.val > stack[-1].val:
                    parent = stack.pop()
                parent.right = newNode
            stack.append(newNode)
        return root
    
    