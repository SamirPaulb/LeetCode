class Solution:
    def frequencySort(self, s: str) -> str:
        chr2count = {}
        for i in s:
            if i not in chr2count:
                chr2count[i] = 1
            else:
                chr2count[i] += 1
                
        count2chr = {}
        for i in chr2count:
            count = chr2count[i]
            if count not in count2chr:
                count2chr[count] = [i]
            else:
                count2chr[count].append(i)
        
        counts = sorted(list(count2chr.keys()), reverse = True)
        res = ""
        for c in counts:
            for i in count2chr[c]:
                res += i * c
        
        return res