class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(version1.split('.'))
        v2 = list(version2.split('.'))
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            a1 = v1[i] if i < len(v1) else 0
            a2 = v2[j] if j < len(v2) else 0
            if int(a1) < int(a2):
                return -1
            elif int(a1) > int(a2):
                return 1
            i += 1
            j += 1
        return 0
