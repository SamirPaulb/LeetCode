# https://www.youtube.com/watch?v=WR6-DrAsNpc
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root == None or (root.left == None and root.right == None):
            return
        
        if root.left:
            self.flatten(root.left)
            
            tmp = root.right
            root.right = root.left
            root.left = None
            
            t = root.right
            while t.right != None:
                t = t.right
            t.right = tmp
            
        self.flatten(root.right)
        
        return root