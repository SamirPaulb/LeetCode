class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)

    def pop(self) -> None:
        if len(self.s) != 0:
            return self.s.pop(-1)
        return []

    def top(self) -> int:
        if len(self.s) != 0:
            return self.s[-1]
        return []

    def getMin(self) -> int:
        return min(self.s)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()