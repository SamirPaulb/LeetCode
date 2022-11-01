class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        i = 0
        for house in houses:
            while i+1 < len(heaters) and heaters[i+1] < house:
                i += 1
            res = max(res, min(abs(h - house) for h in heaters[i:i+2])) 
        
        return res