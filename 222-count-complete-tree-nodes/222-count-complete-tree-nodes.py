# https://leetcode.com/problems/count-complete-tree-nodes/
# https://youtu.be/u-yWemKGWO0

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)
        
        if leftHeight == rightHeight: 
            return 2 ** leftHeight - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)         
        
    
    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
    
# Height = H = log(n) where n = total number of nodes
# Time: O(H * H) = O(log(n)^2) = O(Log^2 n)
# Auxiliary Space: O(H) = O(log(n))
    