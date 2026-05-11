from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        for ind in range (0, len(nums), 1):
            appear_ind: int = abs(nums[ind]) - 1
            if nums[appear_ind] > 0:
                nums[appear_ind] = -nums[appear_ind]

        for ind in range(0, len(nums), 1):
            if nums[ind] > 0:
                result.append(ind + 1)

        return result
