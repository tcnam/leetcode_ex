import typing as t

class Solution:
    def makeGood(self, s: str) -> str:
        stack: t.List[str] = []
        for char in s:
            if stack and char != stack[-1] and char.upper() == stack[-1].upper():
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)