class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        matTrans = [list(x) for x in zip(*mat)]
        
        count = 0
        
        for row in mat:
            if row.count(1) != 1:
                continue

            oneIndex = row.index(1)
            
            if matTrans[oneIndex].count(1) == 1:
                count += 1
                
        return count
            