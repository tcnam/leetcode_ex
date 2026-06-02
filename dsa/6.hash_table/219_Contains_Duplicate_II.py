import typing as t

class Solution:
    def containsNearbyDuplicate(self, nums: t.List[int], k: int) -> bool:
        unique_dict: t.Dict[int, int] = {}
        for ind in range(0, len(nums), 1):
            if nums[ind] in unique_dict.keys():
                if abs(ind - unique_dict.get(nums[ind])) <= k:
                    return True
            unique_dict[nums[ind]] = ind
        return False
