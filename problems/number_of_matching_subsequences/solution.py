class Solution:
    def numMatchingSubseq(self, S, words):
        def isSubseq(word):
            curr = 0
            for symbol in word:
                ind = bisect_left(places[symbol], curr)
                if ind >= len(places[symbol]):
                    return False
                curr = places[symbol][ind] + 1
            
            return True
        
        places = defaultdict(list)
        for i, symbol in enumerate(S):
            places[symbol].append(i)
        
        return sum(isSubseq(word) for word in words)