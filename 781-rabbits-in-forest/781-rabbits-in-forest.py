class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        for i in range(len(answers)):
            if (answers[i] + 1) not in dic:
                dic[answers[i]+1] = 1
            else:
                dic[answers[i]+1] += 1
        
        res = 0
        for key in dic:
            a = dic[key]
            a //= key
            res += key * a
            if dic[key] % key > 0:
                res += key
        
        return res