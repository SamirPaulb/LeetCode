class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
            return
        if self.max_stack[-1] > x:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            self.max_stack.pop(-1)
            return self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        if len(self.max_stack) != 0:
            return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        val = self.peekMax()
        buff = []
        while self.top() != val:
            buff.append(self.pop())
        self.pop()
        while len(buff) != 0:
            self.push(buff.pop(-1))
        return val
