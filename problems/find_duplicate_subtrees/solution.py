class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        d = {}
        
        def postorder(root):
            if not root: return "#"
            l = postorder(root.left)
            r = postorder(root.right)
            key = l + " " + r + " " + str(root.val)
            
            if not key in d: d[key] = 1
            else: d[key] += 1
            
            if d[key] == 2: ans.append(root)
            
            return key
        
        postorder(root)
        
        return ans