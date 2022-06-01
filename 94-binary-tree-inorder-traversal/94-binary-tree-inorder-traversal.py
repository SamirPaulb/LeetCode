# Morris Traversal Inorder

class Solution:
    def inorderTraversal(self, root):
        res = []
        cur = root
        
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    cur = cur.right
                
        return res
    
# Time: O(N)
# Space: O(1)