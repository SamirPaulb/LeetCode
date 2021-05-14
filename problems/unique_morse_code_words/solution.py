class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        A = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        Samir = []
        for i in range(len(words)):
            result = ""
            for j in range(len(words[i])):
                Ind = ord(words[i][j]) - 97
                result += A[Ind]
            Samir.append(result)
        Samir = set(Samir)
        return len(Samir)