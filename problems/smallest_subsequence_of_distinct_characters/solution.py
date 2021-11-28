class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # searching an element from a Hash Set takes O(N) time
        visited = set()  # Hash Set
        stack = []
        lastIndex = {ch: i for i, ch in enumerate(s)}
        
        for i, ch in enumerate(s):
            if ch not in visited:
                while stack and stack[-1] > ch and lastIndex[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(ch)
                visited.add(ch)
        
        return "".join(stack)
    