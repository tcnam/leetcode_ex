class Solution:
    def myAtoi(self, s: str) -> int:
        val: int = 0
        sign: int = 1
        start_read_num: bool = False
        for char in s:
            if char == ' ':
                if not start_read_num:
                    continue
                else:
                    break
            
            if char == '-':
                if not start_read_num:
                    start_read_num = True
                    sign = -1
                    continue
                else:
                    break
            
            if char == '+':
                if not start_read_num:
                    start_read_num = True
                    continue
                else:
                    break
            
            if ord(char) >= ord('0') and ord(char) <= ord('9'):
                if not start_read_num:
                    start_read_num = True
                val = val * 10 + int(char)
            else:
                break
        
        result: int = val * sign

        if result < pow(-2,31):
            result = pow(-2,31)
        
        if result > pow(2,31) - 1:
            result = pow(2,31) - 1

        return result

                
