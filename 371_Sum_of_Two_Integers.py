class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # https://leetcode.com/discuss/111582/java-simple-easy-understand-solution-with-explanation
        # in Python this problem is much different because of the negative number
        # https://leetcode.com/discuss/111705/one-positive-one-negative-case-successful-for-python-rules
        import ctypes
        sum = 0
        carry = ctypes.c_int32(b)
        while carry.value != 0:
            sum = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = sum
        return sum