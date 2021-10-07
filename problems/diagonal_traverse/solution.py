class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Making a dictionary of keys = (row + col) as in a Diagonal treversal line (index of row + index of col) = constant. And values of Dictionary are elements of mat
        myDict = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i+j) not in myDict:
                    myDict[i+j] = [mat[i][j]]
                else:
                    myDict[i+j].append(mat[i][j])
                    
        #print(myDict)
        
        ans = []
        # adding values of myDict Diagonally in zigzag manner
        zigzag = False
        for i in myDict:
            if zigzag == True:
                ans += myDict[i]
                zigzag = False
            else:
                ans += myDict[i][::-1]
                zigzag = True
    
        return ans
            