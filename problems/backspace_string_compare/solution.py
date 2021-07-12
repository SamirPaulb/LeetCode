class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s_ = []
        t_ = []
        for i in range(len(s)):
            if len(s_) == 0 and s[i] != "#":
                s_.append(s[i])
            elif len(s_) == 0 and s[i] == "#":
                continue
            elif len(s_) != 0 and s[i] == "#":
                s_.pop(-1)
            elif len(s_) != 0 and s[i] != "#":
                s_.append(s[i])

        for i in range(len(t)):
            if len(t_) == 0 and t[i] != "#":
                t_.append(t[i])
            elif len(t_) == 0 and t[i] == "#":
                continue
            elif len(t_) != 0 and t[i] == "#":
                t_.pop(-1)
            elif len(t_) != 0 and t[i] != "#":
                t_.append(t[i])
        
        s_ans = ""
        t_ans = ""
        
        for i in s_:
            s_ans += i
        
        for i in t_:
            t_ans += i
       
        return s_ans == t_ans