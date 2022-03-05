class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.preIndex = 0
        def dfs(postStart, postEnd):
            if postStart > postEnd or self.preIndex >= len(preorder): return None
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            if postStart == postEnd or self.preIndex >= len(preorder): return root
            postIndex = postorder.index(preorder[self.preIndex])
            root.left = dfs(postStart, postIndex)
            root.right = dfs(postIndex+1, postEnd-1)
            
            return root
        
        return dfs(0, len(preorder))