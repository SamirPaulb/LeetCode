class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        q, res = [root], []
        zigzag = True
        while q:
            tmpArr = []
            for i in range(len(q)):
                tmpNode = q.pop(0)
                tmpArr.append(tmpNode.val)
                if tmpNode.left: q.append(tmpNode.left)
                if tmpNode.right: q.append(tmpNode.right)
            if zigzag: 
                res.append(tmpArr)
                zigzag = False
            else: 
                res.append(tmpArr[::-1])
                zigzag = True
        
        return res
            