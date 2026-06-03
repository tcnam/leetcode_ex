import typing as t

class Solution:
    def subarraySum(self, nums: t.List[int], k: int) -> int:
        result: int = 0
        acc_sum: int = 0
        prefix_sum_dict: t.Dict[int, int] = {
            0: 1
        }

        for ind in range(0, len(nums), 1):
            acc_sum += nums[ind]
            if (acc_sum - k) in prefix_sum_dict.keys():
                result += prefix_sum_dict.get(acc_sum - k)

            prefix_sum_dict[acc_sum] = prefix_sum_dict.get(acc_sum, 0) + 1
        
        return result