class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        # https://leetcode.com/problems/binary-tree-paths/
        def binaryTreePaths(root, s):
            if not root: return
            if root.left == None and root.right == None:
                s += str(root.val)
                self.ans += (int(s))
            if root.left:
                binaryTreePaths(root.left, s = s + str(root.val))
            if root.right:
                binaryTreePaths(root.right, s = s + str(root.val))
                
        binaryTreePaths(root, "")
        
        return self.ans

    
