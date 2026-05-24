import typing as t

class Solution:
    def calculate(self, s: str) -> int:
        stack: t.List[int] = []
        ind: int = 0
        result: int = 0
        curr_sign: int = 1

        while ind < len(s):
            char: str = s[ind]

            if char.isdigit():
                parse_num: t.Tuple[int] = self._parseNum(s, ind)
                num: int = parse_num[0]
                new_ind: int = parse_num[1]

                ind = new_ind
                stack.append(num * curr_sign)
                curr_sign = 1

            elif char == "+":
                curr_sign = 1

            elif char == "-":
                curr_sign = -1

            elif char == "*" or char == "/":
                while not s[ind].isdigit():
                    ind += 1

                parse_num: t.Tuple[int] = self._parseNum(s, ind)
                num: int = parse_num[0]
                new_ind: int = parse_num[1]

                ind = new_ind
                prev_num: int = stack.pop()
                if char == "*":
                    stack.append(prev_num * num)
                
                if char == "/":
                    stack.append(int(prev_num / num))
            else:
                pass
            ind += 1
        
        for val in stack:
            result += val
            
        return result
    
    def _parseNum(self, s: str, ind: int) -> t.Tuple[int]:
        num: int = 0
        start_ind: int = ind
        while start_ind < len(s) and s[start_ind].isdigit():
            num = num * 10 + int(s[start_ind])
            start_ind += 1
        return (num, start_ind - 1)