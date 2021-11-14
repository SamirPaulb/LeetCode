class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = {}
        ans = []
        def solve(root):
            if not root: return "#"
            l = solve(root.left)
            r = solve(root.right)
            key = l + " " +  r + " " +  str(root.val)
            if key not in dic: dic[key] = 1
            else: dic[key] += 1
            if dic[key] == 2: ans.append(root)
            
            return key
        
        solve(root)
        return ans