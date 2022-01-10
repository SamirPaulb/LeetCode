class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Fractional Knapsack Problem
        # numberOfBoxes = Weight array
        # numberOfUnitsPerBox = Value array
        
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        res = 0
        for i in range(len(boxTypes)):
            if boxTypes[i][0] > truckSize:
                res += truckSize * boxTypes[i][1]
                boxTypes[i][0] -= truckSize
                break
            else:
                res += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
        
        return res