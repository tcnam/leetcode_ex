import typing as t

class Solution:
    def minLength(self, s: str) -> int:
        char_dict: t.Dict[str, str] = {
            "B": "A"
            , "D": "C"
        }
        stack: t.List[str] = []

        for char in s:
            if stack and char in char_dict.keys() and stack[-1] == char_dict.get(char):
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack)
