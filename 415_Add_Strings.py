class Solution(object):
    # def addStrings(self, num1, num2):
    #     """
    #     :type num1: str
    #     :type num2: str
    #     :rtype: str
    #     """
    #     if num1 is None:
    #         num1 = '0'
    #     if num2 is None:
    #         num2 = '0'
    #     res = []
    #     carry = 0
    #     ls = min(len(num1), len(num2))
    #     pos = -1
    #     while pos + ls >= 0:
    #         curr = int(num1[pos]) + int(num2[pos]) + carry
    #         res.insert(0, str(curr % 10))
    #         carry = curr / 10
    #         pos -= 1
    #     while pos + len(num1) >= 0:
    #         curr = int(num1[pos]) + carry
    #         res.insert(0, str(curr % 10))
    #         carry = curr / 10
    #         pos -= 1
    #     while pos + len(num2) >= 0:
    #         curr = int(num2[pos]) + carry
    #         res.insert(0, str(curr % 10))
    #         carry = curr / 10
    #         pos -= 1
    #     if carry != 0:
    #         res.insert(0, str(carry))
    #     return ''.join(res)

    def addStrings(self, num1, num2):
        res = []
        pos1 = len(num1) - 1
        pos2 = len(num2) - 1
        carry = 0
        # This conditon is great
        # https://leetcode.com/problems/add-strings/discuss/90436/Straightforward-Java-8-main-lines-25ms
        while pos1 >= 0 or pos2 >= 0 or carry == 1:
            digit1 = digit2 = 0
            if pos1 >= 0:
                digit1 = ord(num1[pos1]) - ord('0')
            if pos2 >= 0:
                digit2 = ord(num2[pos2]) - ord('0')
            res.append(str((digit1 + digit2 + carry) % 10))
            carry = (digit1 + digit2 + carry) / 10
            pos1 -= 1
            pos2 -= 1
        # reverse res
        return ''.join(res[::-1])
