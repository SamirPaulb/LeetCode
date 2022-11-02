class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        s = sum(wall[0])
        dct = {0:n, n:n}
        
        for w in wall:
            i = 0
            for j in w[:-1]:
                i += j
                if i in dct: dct[i] -= 1
                else: dct[i] = n - 1
                    
        # print(dct)
        return min(list(dct.values()))