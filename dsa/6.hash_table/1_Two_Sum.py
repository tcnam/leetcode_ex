import typing as t

class Solution:
    def twoSum(self, nums: t.List[int], target: int) -> t.List[int]:
        unique_dict: t.Dict[int, int] = {}
        for ind in range(0, len(nums), 1):
            if nums[ind] in unique_dict.keys():
                return [ind, unique_dict.get(nums[ind])]
            else:
                unique_dict[target - nums[ind]] = ind
        
        return [-1, -1]
