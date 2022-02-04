class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            curr = flowerbed[i]
            if i - 1 >= 0:
                curr += flowerbed[i - 1]
            if i + 1 < len(flowerbed):
                curr += flowerbed[i + 1]
            if curr == 0:
                count += 1
                flowerbed[i] = 1
                if count >= n:
                    return True
        return False
