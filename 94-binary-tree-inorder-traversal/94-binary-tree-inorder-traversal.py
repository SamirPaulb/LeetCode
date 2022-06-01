class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        cur = root
        
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre and pre.right:
                    pre = pre.right
                pre.right = cur
                # disconnecting the left pointer so that we will not return here again
                tmp = cur.left
                cur.left = None
                cur = tmp
                
        return res