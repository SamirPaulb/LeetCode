class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        q, res = [root], []
        while q:
            tmpArr = []
            for i in range(len(q)):
                tmpNode = q.pop(0)
                tmpArr.append(tmpNode.val)
                if tmpNode.left: q.append(tmpNode.left)
                if tmpNode.right: q.append(tmpNode.right)
            res.append(tmpArr)
        
        return res[::-1]
    
    