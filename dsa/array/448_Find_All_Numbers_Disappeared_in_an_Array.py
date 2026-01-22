from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        for i in range(0, len(nums), 1):
            ind: int = abs(nums[i]) - 1
            nums[ind] = -1*abs(nums[ind])
        for i in range(0, len(nums), 1):
            if nums[i] > 0:
                result.append(i+1)
        return result
