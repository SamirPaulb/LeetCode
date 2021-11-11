class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        def solve(root):
            if not root: return 0
            s = solve(root.left) + root.val + solve(root.right)  # Postorder Traversal
            if s not in dic: dic[s] = 1
            else: dic[s] += 1
            return s
        solve(root)
        m = max(list(dic.values()))
        ans = []
        for i in dic:
            if dic[i] == m:
                ans.append(i)
        
        print(dic)
        return ans
        