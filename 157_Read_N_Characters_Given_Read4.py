# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        pos, eof = 0, False
        while not eof and pos < n:
            buffer = [''] * 4
            sz = read4(buffer)
            if sz < 4:
                eof = True
            for i in range(sz):
                buf[pos + i] = buffer[i]
            pos += min(n - pos, sz)
        return pos