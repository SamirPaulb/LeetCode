# class Queue(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack1 = []
#         self.stack2 = []
#
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         while len(self.stack1) > 0:
#             curr = self.stack1.pop()
#             self.stack2.append(curr)
#         self.stack1.append(x)
#         while len(self.stack2) > 0:
#             curr = self.stack2.pop()
#             self.stack1.append(curr)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         self.stack1.pop()
#
#
#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.stack1[-1]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.stack1) == 0

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        self.stack2.pop()


    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) + len(self.stack2) == 0