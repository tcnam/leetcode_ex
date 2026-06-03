import typing as t

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freq_dict: t.Dict[int, int] = {}
        max_val: int = -1
        
        for ind in range(lowLimit, highLimit + 1, 1):
            cur_box_num: int = self.boxNumber(ind)
            freq_dict[cur_box_num] = freq_dict.get(cur_box_num, 0) + 1
            if freq_dict.get(cur_box_num) > max_val:
                max_val = freq_dict.get(cur_box_num)

        return max_val
        
    
    def boxNumber(self, number: int) -> int:
        result: int = 0
        temp_num: int = number
        while temp_num > 0:
            result += temp_num % 10
            temp_num = int(temp_num /10)
        return result