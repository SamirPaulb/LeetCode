class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        combinations = []
        curr = [0] * len(digits)
        letter_idx = [0] * len(digits)
        i = 0
        
        while True:
            if letter_idx[i] < len(d[digits[i]]):
                curr[i] = d[digits[i]][letter_idx[i]]
                if i == len(digits) - 1:
                    combinations.append(''.join(curr))
                    letter_idx[i] += 1
                else:
                    i += 1
            elif i > 0:
                i -= 1
                letter_idx[i] += 1
                for j in range(i + 1, len(digits)):
                    letter_idx[j] = 0
            else:
                break
                
        return combinations