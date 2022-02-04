class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ls = len(height)
        if ls == 0:
            return 0
        res, left = 0, 0
        while left < ls and height[left] == 0:
            left += 1
        pos = left + 1
        while pos < ls:
            if height[pos] >= height[left]:
                # there is a right bar which is no less than left bar
                res += self.rain_water(height, left, pos)
                left = pos
                pos += 1
            elif pos == ls - 1:
                # left bar is higher than all right bar
                max_value, max_index = 0, pos
                for index in range(left + 1, ls):
                    if height[index] > max_value:
                        max_value = height[index]
                        max_index = index
                res += self.rain_water(height, left, max_index)
                left = max_index
                pos = left + 1
            else:
                pos += 1
        return res

    def rain_water(self, height, start, end):
        # computer rain water
        if end - start <= 1:
            return 0
        min_m = min(height[start], height[end])
        res = min_m * (end - start - 1)
        step = 0
        for index in range(start + 1, end):
            if height[index] > 0:
                step += height[index]
        return res - step

    # def trap(self, height):
    #     ls = len(height)
    #     if ls == 0:
    #         return 0
    #     height.append(0)
    #     height.insert(0, 0)
    #     left = [0] * ls
    #     right = [0] * ls
    #     cur_left, cur_right = 0, 0
    #     for i in range(1, ls + 1):
    #         cur_left = max(cur_left, height[i - 1])
    #         # left[i] store max bar from left
    #         left[i - 1] = cur_left
    #     for i in reversed(range(ls)):
    #         cur_right = max(cur_right, height[i + 1])
    #         # right[i] store max bar from right
    #         right[i] = cur_right
    #     res = 0
    #     for i in range(ls):
    #         curr = min(left[i], right[i])
    #         if curr > height[i]:
    #             res += curr - height[i]
    #     return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.trap([2,6,3,8,2,7,2,5,0])


