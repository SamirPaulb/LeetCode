class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for  i in range(len(image)):
            image[i].reverse()
        for  i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        return image
                    
            
            