class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0  # nonelocal variable => self.preorder_index = nonlocal preorder_index
        def constractTree(left, right):
            if left > right: return None
            
            rootValue = preorder[self.preorder_index]
            root = TreeNode(rootValue)
            
            self.preorder_index += 1
            
            if left == right: return root
            
            root.left = constractTree(left, inorder_index[rootValue] - 1)
            root.right = constractTree(inorder_index[rootValue] + 1, right)
            
            return root
        
        inorder_index = {}
        for i, element in enumerate(inorder):
            inorder_index[element] = i
        
        return constractTree(0, len(preorder) - 1)