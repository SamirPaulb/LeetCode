Morse_tab = [".-","-...","-.-.",
             "-..",".","..-.","--.","....",
             "..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--",
             "-..-","-.--","--.."]

class Solution(object):
    # https://leetcode.com/problems/unique-morse-code-words/solution/
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        ans_set = set()
        for word in words:
            morsed = ""
            for c in word:
                morsed += Morse_tab[ord(c) - ord('a')]
            
            ans_set.add(morsed)
        return len(ans_set)
