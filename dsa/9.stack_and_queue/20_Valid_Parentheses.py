import typing as t

class Solution:
    def isValid(self, s: str) -> bool:
        stack: t.List[int] = []
        bracket_dict: t.Dict[str, str] = {
            "}": "{"
            ,")": "("
            ,"]": "["
        }
        for char in s:
            if (
                char in bracket_dict.keys() 
                and stack
                and stack[-1] == bracket_dict.get(char)
            ):
                stack.pop()
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True
