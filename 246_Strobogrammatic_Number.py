class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # hash table
        dic = {'0':'0', '6':'9', '9': '6', '1' :'1', '8': '8'}
        temp_s = ''
        for c in num[::-1]:
            if c not in dic:
                return False
            temp_s += dic[c]
        if int(temp_s) == int(num):
            return True
        return False

    # def isStrobogrammatic(self, num):
    #     # https://discuss.leetcode.com/topic/20840/1-liners-python
    #     return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))
        