class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        res_list = []
        curr = []
        count, pos = 0, 0
        while pos < len(words):
            word = words[pos]
            if len(word) > maxWidth:
                pos += 1
            if len(word) + count + len(curr)<= maxWidth:
                count += len(word)
                curr.append(word)
                pos += 1
            else:
                res_list.append(curr)
                curr = []
                count = 0
        if len(curr) > 0:
            res_list.append(curr)
        # print res_list
        for index, curr in enumerate(res_list):
            text = ''
            remain = sum([len(t) for t in curr])
            if len(curr) == 1:
                # single word
                text = curr[0] + ' ' * (maxWidth - remain)
            elif index == len(res_list) - 1:
                # last line
                text = ' '.join(curr)
                text += ' ' * (maxWidth - remain - len(curr) + 1)
            else:
                # multiple
                step = (maxWidth - remain) / (len(curr) - 1 )
                extra = (maxWidth - remain) % (len(curr) - 1 )
                for index in range(len(curr) - 1):
                    text += curr[index] + ' ' * step
                    if extra > 0:
                        # assign from left
                        text += ' '
                        extra -= 1
                text += curr[-1]
            res.append(text)
        return res

    # def fullJustify(self, words, maxWidth):
    #     i, N, result = 0, len(words), []
    #     while i < N:
    #         # decide how many words to be put in one line
    #         oneLine, j, currWidth, positionNum, spaceNum = [words[i]], i + 1, len(words[i]), 0, maxWidth - len(words[i])
    #         while j < N and currWidth + 1 + len(words[j]) <= maxWidth:
    #             oneLine.append(words[j])
    #             currWidth += 1 + len(words[j])
    #             spaceNum -= len(words[j])
    #             positionNum, j = positionNum + 1, j + 1
    #         i = j
    #         # decide the layout of one line
    #         if i < N and positionNum:
    #             spaces = [' ' * (spaceNum / positionNum + (k < spaceNum % positionNum)) for k in range(positionNum)] + [
    #                 '']
    #         else:  # last line or the line only has one word
    #             spaces = [' '] * positionNum + [' ' * (maxWidth - currWidth)]
    #         result.append(''.join([s for pair in zip(oneLine, spaces) for s in pair]))
    #     return result

if __name__ == '__main__':
    s = Solution()
    print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."],30)
