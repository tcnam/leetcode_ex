from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length: int = len(nums)
        left_sum_array: List[int] = [0]*length
        right_sum_array: List[int] = [0]*length
        left_sum_acc: int = 0
        right_sum_acc: int = 0

        for ind in range(0, length, 1):
            left_sum_acc += nums[ind]
            right_sum_acc += nums[length - 1 - ind]
            left_sum_array[ind] = left_sum_acc
            right_sum_array[length - 1 - ind] = right_sum_acc
        
        for ind in range(0, length, 1):
            left_sum: int = (
                left_sum_array[ind - 1] 
                if ind - 1 >= 0
                else 0
            )
            right_sum: int = (
                right_sum_array[ind + 1] 
                if ind + 1 < length 
                else 0
            )
            if left_sum == right_sum:
                return ind
            
        return -1