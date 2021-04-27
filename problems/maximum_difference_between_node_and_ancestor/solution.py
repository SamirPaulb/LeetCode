class Solution(object):
    
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def utility_fun(root, res):
            if not root:
                return 2147483648, -2147483648, res
            if not root.left and not root.right:
                return root.val, root.val, res
            left_t, lmax_t, res = utility_fun(root.left, res)
            right_t, rmax_t, res = utility_fun(root.right, res)
            m_val = min(left_t, right_t)
            max_val = max(lmax_t, rmax_t)
                
            res = max(res, max(abs(root.val-m_val), abs(root.val-max_val)))
            # print res
            return min(m_val, root.val), max(max_val, root.val), res
        
        x, x2, res = utility_fun(root, -2147483648)
        return abs(res)