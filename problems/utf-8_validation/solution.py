class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        seveneth_mask = 1 << 7
        sixth_mask = 1 << 6
        no_bytes = 0
        
        if len(data) == 1:
            return not(data[0] & seveneth_mask)
        
        for num in data:
            if no_bytes == 0:
                mask = 1 << 7
                
                while num & mask:
                    no_bytes += 1
                    mask >>= 1
                    
                if no_bytes == 0:
                    continue
                    
                if no_bytes == 1 or no_bytes > 4:
                    return False
            else:
                if not(num & seveneth_mask and not(num & sixth_mask)):
                    return False
            no_bytes -= 1
        return no_bytes == 0