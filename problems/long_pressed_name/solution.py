class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ni = 0       # index of name
        ti = 0       # index of typed
        while ni <= len(name) and ti < len(typed):
            if ni < len(name) and typed[ti] == name[ni]:
                ti += 1
                ni += 1
            elif typed[ti] == name[ni-1] and ni != 0:
                ti += 1
            else:
                return False
            
        return ni == len(name) and ti == len(typed)