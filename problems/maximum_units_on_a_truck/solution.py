class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        ans = 0
        for box_num, units in sorted(boxTypes, key = lambda x:-x[1]):
            if not truckSize: break
            ans += min(box_num, truckSize) * units
            truckSize -= min(box_num, truckSize)

        return ans
