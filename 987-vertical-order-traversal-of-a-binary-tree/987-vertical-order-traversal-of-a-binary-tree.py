# If some nodes of same horizontal level comes in same vertical level then
# we should only sort those nodes.
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = {}
        def solve(root, d, l):
            if not root: return
            
            if d not in self.dic:
                self.dic[d] = [(l, root.val)]
            else:
                self.dic[d].append((l, root.val))
                
            solve(root.left, d-1, l+1)
            solve(root.right, d+1, l+1)
        
        solve(root, 0, 0)
        keys = sorted(list(self.dic.keys()))
        
        res = []
        for key in keys:
            values = self.dic[key]
            values.sort()  # sorting is done based on level then for same level nodes based on values
            res.append([r[1] for r in values])
            
        return res