class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.internal = []
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.internal.append(number)
        if number in self.dic:
            # more than once
            self.dic[number] = True
            return
        # once
        self.dic[number] = False

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for v in self.internal:
            if value - v in self.dic:
                if v << 1 == value and not self.dic[v]:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
