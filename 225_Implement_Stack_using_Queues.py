# class Stack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.queue1 = []
#         self.queue2 = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         self.queue1.append(x)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         while len(self.queue1) > 1:
#             curr = self.queue1.pop(0)
#             self.queue2.append(curr)
#         if len(self.queue1) == 1:
#             self.queue1.pop(0)
#         while len(self.queue2):
#             curr = self.queue2.pop(0)
#             self.queue1.append(curr)
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         while len(self.queue1) > 1:
#             curr = self.queue1.pop(0)
#             self.queue2.append(curr)
#         return self.queue1[0]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.queue1) + len(self.queue2) == 0


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.curr_top = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue2.append(x)
        self.curr_top = x
        while len(self.queue1):
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue1.pop(0)
        if len(self.queue1):
            self.curr_top = self.queue1[0]

    def top(self):
        """
        :rtype: int
        """
        if self.empty() is False:
            return self.curr_top

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0

