import typing as t

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s: t.List[str] = []
        stack_t: t.List[str] = []
        t.List
        for char in s:
            if char == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        
        for char in t:
            if char == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)
        
        if len(stack_s) == len(stack_t):
            for ind in range(0, len(stack_s), 1):
                if stack_s[ind] != stack_t[ind]:
                    return False
            return True
        else:
            return False
