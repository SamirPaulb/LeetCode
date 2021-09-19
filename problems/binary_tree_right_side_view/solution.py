class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Implement Level Order Traversal and append right node of each level to the answer
        final_ans = []
        q = []
        q.append(root)
        if not root: return
        while q:
            tmp_ans = []
            for i in range(len(q)):
                node = q.pop(0)
                tmp_ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            final_ans.append(tmp_ans[-1])
        return final_ans