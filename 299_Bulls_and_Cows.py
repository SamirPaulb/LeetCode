class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        check = {}
        ls = len(secret)
        bull, cow = 0, 0
        different = []
        for i in range(ls):
            if guess[i] == secret[i]:
                bull += 1
            else:
                # store possible index and count for cow
                different.append(i)
                try:
                    check[secret[i]] += 1
                except KeyError:
                    check[secret[i]] = 1
        for i in different:
            try:
                if check[guess[i]] > 0:
                    cow += 1
                    check[guess[i]] -= 1
            except:
                pass
        return "%dA%dB" % (bull, cow)


if __name__ == "__main__":
    s = Solution()
    print s.getHint("1122", "1222")
