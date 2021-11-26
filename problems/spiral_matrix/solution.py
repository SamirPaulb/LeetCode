class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, low, left, right, res = 0, len(matrix), 0, len(matrix[0]), []
        
        while up < low and left < right:
            # For 1 -> 2 -> 3
            for i in range(left, right):
                res.append(matrix[up][i])
            up += 1
            # For 6 -> 9 
            for i in range(up, low):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (up < low and left < right): break
            # For 8 -> 7
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[low - 1][i])
            low -= 1
            # For 4
            for i in range(low - 1, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
        
    
'''
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
[[6,9,7]]
[[1,2],[3,4]]
'''