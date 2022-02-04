class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        v_map = {}
        A.sort(key=lambda x: abs(x))
        for n in A:
            v_map[n] = v_map.get(n, 0) + 1
        for n in A:
            if v_map[n] <= 0:
                continue
            if 2 * n in v_map and v_map[2 * n] > 0:
                v_map[n] -= 1
                v_map[2 * n] -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.canReorderDoubled([3, 1, 3, 6])
    print s.canReorderDoubled([2, 1, 2, 6])
    print s.canReorderDoubled([4, -2, 2, -4])
    print s.canReorderDoubled([1, 2, 4, 16, 8, 4])
