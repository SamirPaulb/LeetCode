class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            a = 0
        elif ruleKey == "color":
            a = 1
        elif ruleKey == "name":
            a = 2
        
        s = 0
        
        for i in range(len(items)):
            if items[i][a] == ruleValue:
                s = s+1
        return s