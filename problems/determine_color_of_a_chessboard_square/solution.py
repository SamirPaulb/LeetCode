class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        s = coordinates
        if (ord(s[0])-96) % 2 ==0 and int(s[1] )% 2 !=0:
            return True
        elif (ord(s[0])-96) % 2 !=0 and int(s[1] )% 2 ==0:
            return True
        elif (ord(s[0])-96) % 2 !=0 and int(s[1] )% 2 !=0:
            return False
        else:
            return False
        
        
        