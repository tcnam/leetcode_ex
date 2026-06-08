import typing as t

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: t.List[str] = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
