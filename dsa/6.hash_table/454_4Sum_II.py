import typing as t

class Solution:
    def fourSumCount(self, nums1: t.List[int], nums2: t.List[int], nums3: t.List[int], nums4: t.List[int]) -> int:
        freq_sum_dict: t.Dict[int] = {}
        result: int = 0

        for ind1 in range(0, len(nums1), 1):
            for ind2 in range(0, len(nums2), 1):
                temp_sum: int = -(nums1[ind1] + nums2[ind2])
                if temp_sum not in freq_sum_dict.keys():
                    freq_sum_dict[temp_sum] = 1
                else:
                    freq_sum_dict[temp_sum] = freq_sum_dict.get(temp_sum) + 1
        
        for ind3 in range(0, len(nums3), 1):
            for ind4 in range(0, len(nums4), 1):
                temp_sum: int = nums3[ind3] + nums4[ind4]
                if temp_sum in freq_sum_dict.keys():
                    result += freq_sum_dict.get(temp_sum)
        
        return result
