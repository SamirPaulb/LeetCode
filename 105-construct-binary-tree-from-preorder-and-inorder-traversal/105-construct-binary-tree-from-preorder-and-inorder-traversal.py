# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pi = 0  # PreOrder Index
        inInd = {}
        for i, ch in enumerate(inorder):
            inInd[ch] = i
        
        def solve(l, r):
            if l > r: return None
            
            root = TreeNode(preorder[self.pi])
            self.pi += 1
            i = inInd[root.val]
            
            root.left = solve(l, i-1)
            root.right = solve(i+1, r)
            
            return root
        
        return solve(0, len(inorder)-1)
    
'''    
    
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pi = 0  # PreOrder Index
        inInd = {}
        for i, ch in enumerate(inorder):
            inInd[ch] = i
        
        def solve(preorder, inorder):
            if not preorder or not inorder: return None
            
            root = TreeNode(preorder[0])
            self.pi += 1
            i = inorder.index(root.val)
            
            root.left = solve(preorder[1:i+1], inorder[:i])
            root.right = solve(preorder[1+i:], inorder[i+1:])
            
            return root
        
        return solve(preorder, inorder)