class Solution:
    def countStudents(self, st: List[int], sa: List[int]) -> int:
        lc = 0  # lc = number of times the loop will run
        while lc < 10**5: 
            if len(st) != 0 and st[0] == sa[0]:
                st.pop(0)
                sa.pop(0)
            elif len(st) != 0 and st[0] != sa[0]:
                a = st.pop(0)
                st.append(a)
            lc += 1
        return len(st)