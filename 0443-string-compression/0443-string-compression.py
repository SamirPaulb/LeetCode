class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars)==1:
            return 1
        
        prev_char = chars[0]
        cnt = 1
        ptr = 0
        n = len(chars)

        # This function fills in the chars array with prev_char
        # and digits of cnt if necessary.
        def modify():
            nonlocal prev_char, ptr, cnt
            chars[ptr] = prev_char
            ptr+=1
            if cnt>1:
                cnt = str(cnt)
                for j in range(len(cnt)):
                    chars[ptr]=cnt[j]
                    ptr+=1
            cnt = 1
            prev_char = curr_char

        for i in range(1,n):
            curr_char = chars[i]
            if curr_char==prev_char:
                cnt+=1
            else:
                modify()
        
        modify()
        return ptr            
