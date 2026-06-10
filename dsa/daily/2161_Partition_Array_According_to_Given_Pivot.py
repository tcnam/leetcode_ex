import typing as t

class Solution:
    def pivotArray(self, nums: t.List[int], pivot: int) -> t.List[int]:
        result: t.List[int] = [0] * len(nums)
        before_length: int = 0
        between_length: int = 0
        after_length: int = 0

        for num in nums:
            if num == pivot:
                between_length += 1
            elif num < pivot:
                before_length += 1
            else:
                after_length += 1
        
        ind_before: int = 0
        ind_between: int = before_length
        ind_after: int = before_length + between_length
        
        for num in nums:
            if num < pivot:
                result[ind_before] = num
                ind_before += 1
            elif num > pivot:
                result[ind_after] = num
                ind_after += 1
            else:
                result[ind_between] = num
                ind_between += 1
        
        return result