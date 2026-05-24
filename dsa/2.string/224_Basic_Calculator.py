import typing as t

class Solution:
    def calculate(self, s: str) -> int:
        stack: t.List[int] = []
        curr_sign: int = 1
        curr_result: int = 0
        ind : int = 0

        while ind < len(s):
            char: str = s[ind]
            if char.isdigit():
                start_ind: int = ind
                num: int = 0
                while start_ind < len(s) and s[start_ind].isdigit():
                    num = num * 10 + int(s[start_ind])
                    start_ind += 1
                curr_result += num * curr_sign
                ind = start_ind - 1 

            elif char == "+":
                curr_sign = 1

            elif char == "-":
                curr_sign = -1
            # save states (curr_result and curr_sign) before entering new scope
            elif char == "(":
                stack.append(curr_result)
                stack.append(curr_sign)
                curr_result = 0
                curr_sign = 1
            
            # scope end, add back prev_states have save before
            elif char == ")":
                prev_sign: int = stack.pop()
                prev_result: int = stack.pop()

                curr_result = prev_sign * curr_result + prev_result
            else:
                pass
            
            ind += 1
        
        return curr_result
