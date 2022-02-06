## Time: O(m*n * 4^s) ; where s = len(word), m = no. of rows and n = no. of cols of the word. Since we may end considering every character(m*n) as a start of the word, and from there we have 4 choices to continue to look for the rest of the word (4^s).
#
## Space: O(m*n) ; as each time of dfs calling we are passing a copy of main board.