class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

    # def isRectangleOverlap(self, rec1, rec2):
    #     def intersect(p_left, p_right, q_left, q_right):
    #         return min(p_right, q_right) > max(p_left, q_left)
    #     return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
    #             intersect(rec1[1], rec1[3], rec2[1], rec2[3]))
