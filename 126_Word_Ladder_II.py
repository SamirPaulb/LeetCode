import string
class Solution(object):
    # def findLadders(self, beginWord, endWord, wordlist):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordlist: Set[str]
    #     :rtype: List[List[int]]
    #     """
    #     # https://leetcode.com/discuss/99348/fast-python-solution-using-dbfs-beats-98%25
    #     def construct_paths(begin, end, tree, path, paths):
    #         if begin == end:
    #             paths.append(path)
    #             return
    #         if begin in tree:
    #             for elem in tree[begin]:
    #                 construct_paths(elem, end, tree, path + [elem], paths)
    #
    #     def add_path(tree, word, neigh, is_forw):
    #         if is_forw:
    #             tree[word] = tree.get(word, []) + [neigh]
    #         else:
    #             tree[neigh] = tree.get(neigh, []) + [word]
    #
    #     def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
    #         if len(this_lev) == 0:
    #             return False
    #         if len(this_lev) > len(oth_lev):
    #             return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
    #         for word in (this_lev | oth_lev):
    #             words_set.discard(word)
    #         next_lev = set()
    #         done = False
    #         while len(this_lev):
    #             word = this_lev.pop()
    #             for c in string.ascii_lowercase:
    #                 for index in range(len(word)):
    #                     neigh = word[:index] + c + word[index + 1:]
    #                     if neigh in oth_lev:
    #                         done = True
    #                         add_path(tree, word, neigh, is_forw)
    #                     if not done and neigh in words_set:
    #                         next_lev.add(neigh)
    #                         add_path(tree, word, neigh, is_forw)
    #         return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)
    #
    #     tree, path, paths = {}, [beginWord], []
    #     is_found = bfs_level(set([beginWord]), set([endWord]), tree, True, wordlist)
    #     construct_paths(beginWord, endWord, tree, path, paths)
    #     return paths


    def findLadders(self, beginWord, endWord, wordlist):
        # do not use single dfs or bfs, because both of them
        # try to get result in single direction, which check lots
        # of unnecessary branches
        # https://leetcode.com/discuss/67716/my-30ms-bidirectional-bfs-and-dfs-based-java-solution
        wordlist.discard(beginWord)
        wordlist.discard(endWord)
        hash_map, res = {}, []
        self.bfs(set([beginWord]), set([endWord]), wordlist, False, hash_map)
        print hash_map
        self.dfs(res, [beginWord], beginWord, endWord, hash_map)
        return res

    def bfs(self, forward, backward, wordlist, reverse, hash_map):
        if len(forward) == 0 or len(backward) == 0:
            return
        if len(forward) > len(backward):
            self.bfs(backward, forward, wordlist, not reverse, hash_map)
            return
        is_connected = False
        next_level = set()
        for word in forward:
            for c in string.ascii_lowercase:
                for index in range(len(word)):
                    neigh = word[:index] + c + word[index + 1:]
                    if not reverse:
                        key, value = word, neigh
                    else:
                        key, value = neigh, word
                    if neigh in backward:
                        hash_map[key] = hash_map.get(key, []) + [value]
                        is_connected = True
                    if not is_connected and neigh in wordlist:
                        next_level.add(neigh)
                        hash_map[key] = hash_map.get(key, []) + [value]
                        wordlist.discard(neigh)

        if not is_connected:
            self.bfs(next_level, backward, wordlist, reverse, hash_map)

    def dfs(self, res, path, begin, end, hash_map):
        if begin == end:
            res.append(path)
            return
        try:
            next_step = hash_map[begin]
            for word in next_step:
                self.dfs(res, path + [word], word, end, hash_map)
        except KeyError:
            pass


if __name__ == "__main__":
    s = Solution()
    # print s.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    # print s.findLadders('a', 'b', set(['a', 'b', 'c']))
    # print s.findLadders('hot', 'dog', set(['hot', 'dog']))
    # print s.findLadders("qa", "sq", set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
    print s.findLadders("hot", "dog", set(["hot","cog","dog","tot","hog","hop","pot","dot"]))

