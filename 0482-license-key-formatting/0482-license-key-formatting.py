class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1]
        res = ""
        tmp = ""
        for i in s:
            if i == '-': continue
            tmp += i.upper()
            if len(tmp) == k:
                res += tmp + '-'
                tmp = ""
        
        res += tmp
        if not res: return ""
        if res[-1] == "-": res = res[:-1]
        res = res[::-1]
        return res