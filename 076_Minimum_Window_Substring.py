class Solution(object):
    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #     letters = set(t)
    #     ls = len(s)
    #
    #     # find the first substring that works
    #     first_match = self.first_match(s, t)
    #     if not first_match:
    #         return ''
    #     else:
    #         start, end, extra = first_match
    #         min_window = (end - start, start, end)
    #
    #     # traverse the string and update start and end
    #     while start < end < ls:
    #         discard = s[start]
    #
    #         # move start on to the next letter
    #         while start < end:
    #             start += 1
    #             if s[start] in letters:
    #                 break
    #
    #         # if discarded letter has extra, no need update end
    #         if discard in extra:
    #             extra[discard] -= 1
    #             if extra[discard] == 0:
    #                 extra.pop(discard)
    #             min_window = min(min_window, (end - start, start, end))
    #             continue
    #
    #         # otherwise move end until it points to the discarded letter
    #         while end < ls:
    #             end += 1
    #             if end == ls:
    #                 continue
    #
    #             letter = s[end]
    #             if letter == discard:
    #                 min_window = min(min_window, (end - start, start, end))
    #                 break
    #
    #             if letter in letters:
    #                 extra[letter] += 1
    #
    #     _, start, end = min_window
    #     return s[start: end + 1]
    #
    # def first_match(self, s, t):
    #     letters = set(t)
    #     to_find = collections.defaultdict(lambda: 0)
    #     extra = collections.defaultdict(lambda: 0)
    #
    #     # build hash table
    #     for i in t:
    #         to_find[i] += 1
    #
    #     # find the start position
    #     for index, letter in enumerate(s):
    #         if letter in to_find:
    #             start = index
    #             break
    #     else:
    #         return False
    #
    #     # find the end position
    #     for index, letter in enumerate(s[start:], start):
    #         if letter not in letters:
    #             continue
    #         if letter in to_find:
    #             to_find[letter] -= 1
    #             if to_find[letter] == 0:
    #                 to_find.pop(letter)
    #         else:
    #             extra[letter] += 1
    #         if not to_find:
    #             end = index
    #             break
    #     else:
    #         return False
    #     return start, end, extra
    def minWindow(self, s, t):
        # http://articles.leetcode.com/finding-minimum-window-in-s-which/
        ls_s, ls_t = len(s), len(t)
        need_to_find = [0] * 256
        has_found = [0] * 256
        min_begin, min_end = 0, -1
        min_window = 100000000000000
        for index in range(ls_t):
            need_to_find[ord(t[index])] += 1
        count, begin = 0, 0
        for end in range(ls_s):
            end_index = ord(s[end])
            if need_to_find[end_index] == 0:
                continue
            has_found[end_index] += 1
            if has_found[end_index] <= need_to_find[end_index]:
                count += 1
            if count == ls_t:
                begin_index = ord(s[begin])
                while need_to_find[begin_index] == 0 or\
                    has_found[begin_index] > need_to_find[begin_index]:
                    if has_found[begin_index] > need_to_find[begin_index]:
                        has_found[begin_index] -= 1
                    begin += 1
                    begin_index = ord(s[begin])
                window_ls = end - begin + 1
                if window_ls < min_window:
                    min_begin = begin
                    min_end = end
                    min_window = window_ls
        # print min_begin, min_end
        if count == ls_t:
            return s[min_begin: min_end + 1]
        else:
            return ''


if __name__ == '__main__':
    s = Solution()
    print s.minWindow('a', 'a')

