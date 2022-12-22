class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            x1,y1 = points[i]
            disDict = {}
            for j in range(len(points)):
                if i == j: continue
                x2, y2 = points[j]
                d = (x2-x1)**2 + (y2-y1)**2
                if d in disDict:
                    disDict[d] += 1
                else:
                    disDict[d] = 1
            # print(disDict)
            for key in disDict:
                n = disDict[key]
                res += n*(n-1)
        return res