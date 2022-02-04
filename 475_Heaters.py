class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            # move to next range
            while x >= sum(heaters[i:i + 2]) / 2.:
                i += 1
            # ans = hearter - hourse
            r = max(r, abs(heaters[i] - x))
        return r
