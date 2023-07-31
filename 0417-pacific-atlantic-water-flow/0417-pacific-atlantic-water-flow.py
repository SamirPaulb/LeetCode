class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po, ao = set(), set()
        def dfs(i, j, ocean):
            if not 0<=i<len(heights) or not 0<=j<len(heights[0]) or (i,j) in ocean: return 
            ocean.add((i,j))
            for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=i+x<len(heights) and 0<=j+y<len(heights[0]) and heights[i+x][j+y] >= heights[i][j]:
                    dfs(i+x,j+y,ocean)
        
        for i in range(len(heights)):
            dfs(i, 0, po)
            dfs(i, len(heights[0])-1, ao)
        
        for j in range(len(heights[0])):
            dfs(0, j, po)
            dfs(len(heights)-1, j, ao)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in po and (i,j) in ao: 
                    res.append([i,j])
        return res