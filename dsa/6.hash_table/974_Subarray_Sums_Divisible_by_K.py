import typing as t

class Solution:
    def subarraysDivByK(self, nums: t.List[int], k: int) -> int:
        acc_sum: int = 0
        result: int = 0
        sum_mod_dict: t.Dict[int] = {
            0: 1
        }
        for ind in range(0, len(nums), 1):
            acc_sum += nums[ind]
            cur_mod: int = acc_sum % k
            if cur_mod in sum_mod_dict.keys():
                result += sum_mod_dict.get(cur_mod)
            sum_mod_dict[cur_mod] = sum_mod_dict.get(cur_mod, 0) + 1
        return result