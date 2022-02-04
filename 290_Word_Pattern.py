class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern is None or str is None:
            return True
        # double map
        words_to_pattern = {}
        pattern_to_words = {}
        word_list = str.split(' ')
        if len(word_list) != len(pattern):
            return False
        for index, word in enumerate(word_list):
            curr_p = pattern[index]
            if pattern_to_words.get(curr_p, word) != word or words_to_pattern.get(word, curr_p) != curr_p:
                return False
            pattern_to_words[curr_p] = pattern_to_words.get(curr_p, word)
            words_to_pattern[word] = words_to_pattern.get(word, curr_p)
        return True