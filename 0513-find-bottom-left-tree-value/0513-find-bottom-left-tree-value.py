class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return 
        q = collections.deque()
        q.append(root)
        res = root.val
        while q:
            n = len(q)
            res = q[0].val
            for _ in range(n):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res