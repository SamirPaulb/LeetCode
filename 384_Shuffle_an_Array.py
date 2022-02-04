import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.origin = list(nums)
        self.curr = list(nums)
        self.size = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.curr = list(self.origin)
        return self.curr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(self.size):
            pos = random.randint(0, i)
            # swap i and pos
            self.curr[i], self.curr[pos] = self.curr[pos], self.curr[i]
        return self.curr


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()