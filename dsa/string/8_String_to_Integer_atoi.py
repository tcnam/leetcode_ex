class Solution:
    def myAtoi(self, s: str) -> int:
        result: int = 0
        flag: bool = False
        sign: int = 1
        for char in s:
            if ord(char) == ord(" "):
                if not flag:
                    continue
                else:
                    break
            elif ord(char) == ord("+"):
                if not flag:
                    flag = True
                else:
                    break
            elif ord(char) == ord("-"):
                if not flag:
                    flag = True
                    sign = -1 
                else:
                    break
            elif ord(char) >= ord("0") and ord(char) <= ord("9"):
                flag = True
                result = result * 10 + int(char)
            else:
                break
        result = sign * result
        if result < pow(-2, 31):
            return pow(-2, 31)
        elif result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return result