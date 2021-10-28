class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # The level-order traversal array of a complete binary tree will never have a null node in between non-null nodes. If we encounter a null node, all the following nodes should also be null, otherwise it's not complete.
        if not root: return True
        
        have_null = False
        q = [root]
        
        while q:
            node = q.pop(0)
            if not node: 
                have_null = True
                continue
            if have_null == True: return False
            q.append(node.left)
            q.append(node.right)
        
        return True
    
            