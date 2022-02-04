
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        # letter map
        mp = '0123456789abcdef'
        ans = ''
        for _ in range(8):
            # get last 4 digits
            # num & 1111b
            n = num & 15
            # hex letter for current 1111
            c = mp[n]
            ans = c + ans
            # num = num / 16
            num = num >> 4
        #strip leading zeroes
        return ans.lstrip('0')
    
    # def toHex(self, num):
    #     def tohex(val, nbits):
    #         return hex((val + (1 << nbits)) % (1 << nbits))
    #     return tohex(num, 32)[2:]

    # def toHex(self, num, h=''):
    #     return (not num or h[7:]) and h or self.toHex(num / 16, '0123456789abcdef'[num % 16] + h)
