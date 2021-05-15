class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        STr1 = ""
        for i in range(1,len(s)+1):
            STr1 += f"{i} "


        for i in range(len(s)):
            a = s[i][-1]
            b = s[i].replace(s[i][-1], "")
            STr1 = STr1.replace(a,b)
            STr1 =  STr1.strip()

        return STr1           

            