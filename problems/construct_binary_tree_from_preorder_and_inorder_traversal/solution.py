class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIndex = 0
        inorderIndex = {}
        for i, ch in enumerate(inorder):
            inorderIndex[ch] = i
        
        def constractTree(left, right):
            if left > right: return None
            rootValue = preorder[self.preorderIndex]
            root = TreeNode(rootValue)
            self.preorderIndex += 1
            
            if left == right: return root
            
            root.left = constractTree(left, inorderIndex[rootValue] - 1)
            root.right = constractTree(inorderIndex[rootValue] + 1, right)
            
            return root
        
        return constractTree(0, len(preorder) - 1)