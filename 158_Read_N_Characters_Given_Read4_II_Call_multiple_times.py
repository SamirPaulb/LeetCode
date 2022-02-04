# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.buff = [''] * 4
        self.offset = 0
        self.bufsize = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        pos, eof = 0, False
        while not eof and pos < n:
            if self.bufsize == 0:
                self.bufsize = read4(self.buff)
                eof = self.bufsize < 4
            byte = min(n - pos, self.bufsize)
            for i in range(byte):
                buf[pos + i] = self.buff[self.offset + i]
            self.offset = (self.offset + byte) % 4
            self.bufsize -= byte
            pos += byte
        return pos
