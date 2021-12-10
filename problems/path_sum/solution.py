class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        allPathSums = []
        
        def findAllPathSums(root, s):
            if not root: return s
            if not root.left and not root.right:
                allPathSums.append(root.val + s)
            findAllPathSums(root.left, root.val + s)
            findAllPathSums(root.right, root.val + s)
        
        findAllPathSums(root, 0)
        
        return targetSum in allPathSums
        