If a sequence of words is sorted, then **each adjacent word of the sequence must also be sorted.**
​
👉 Lexicographically Sorted when -
✦ If at first mismatch, mp[a[i]] < mp[b[i]], or
✦ If each letters of both words match and length(a) <= length(b)
​
👉 Not Lexicographically Sorted when -
✦ If at first mismatch, mp[a[i]] > mp[b[i]], or
✦ If each letters of both words match and length(a) > length(b).