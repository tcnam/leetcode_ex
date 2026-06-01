import typing as t

class Solution:
    def minimumOperations(self, nums: t.List[int]) -> int:
        freq_tracker: t.List[int] = [0] * 101
        acc_sum: int = 0
        max_val: int = 0
        result: int = 0
        
        for ind in range(0, len(nums), 1):
            freq_tracker[nums[ind]] += 1
            if nums[ind] > max_val:
                max_val = nums[ind]
        
        for ind in range(0, len(freq_tracker), 1):
            if freq_tracker[ind] > 0:
                curr_num: int = ind - acc_sum
                if curr_num > 0:
                    acc_sum += curr_num
                    max_val -= curr_num
                    result += 1
                
                if max_val == 0:
                    break        
        
        return result
        
        