class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for i in range(len(logs)):
            if logs[i] == "../":
                if len(s) == 0:
                    continue
                else:
                    s.pop(-1)
            elif logs[i] == "./":
                continue
            else:
                s.append(1)
        return len(s)