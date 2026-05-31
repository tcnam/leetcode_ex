import typing as t

class Solution:
    def smallerNumbersThanCurrent(self, nums: t.List[int]) -> t.List[int]:
        # return self.method1(nums)
        return self.method2(nums)
    
    def method2(self, nums: t.List[int]) -> t.List[int]:
        result: t.List[int] = []
        freq_list: t.List[int] = [0] * 101
        freq_acc_sum_list: t.List[int] = []
        acc_sum: int = 0

        for ind in range (0, len(nums), 1):
            freq_list[nums[ind]] += 1
        
        for ind in range(0, len(freq_list), 1):
            acc_sum += freq_list[ind]
            freq_acc_sum_list.append(acc_sum)
        
        for ind in range(0, len(nums), 1):
            small_num_count: int = freq_acc_sum_list[nums[ind] - 1] if nums[ind] > 0 else 0
            result.append(small_num_count)
        
        return result

    
    def method1(self, nums: t.List[int]) -> t.List[int]:
        frequency_dict: t.Dict[int, int] = {}
        cp_nums: t.List[int] = []
        sort_ind_dict: t.Dict[int, int] = {}
        result: t.Dict[int] = []

        for ind in range(0, len(nums), 1):
            cp_nums.append(nums[ind])
            if nums[ind] not in frequency_dict.keys():
                frequency_dict[nums[ind]] = 1
            else:
                frequency_dict[nums[ind]] = frequency_dict.get(nums[ind]) + 1

        self.mergeSort(cp_nums, 0, len(cp_nums) - 1)
        
        for ind in range(0, len(cp_nums), 1):
            sort_ind_dict[cp_nums[ind]] = ind
        
        for ind in range(0, len(nums), 1):
            small_num_count: int = sort_ind_dict[nums[ind]] + 1 - frequency_dict[nums[ind]]
            result.append(small_num_count)

        return result
    
    def merge(self, nums: t.List[int], left: int, mid: int, right: int) -> None:
        nums1: t.List[int] = nums[left: mid + 1]
        nums2: t.List[int] = nums[mid + 1: right + 1]

        ind1: int = 0
        ind2: int = 0
        ind: int = left

        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] < nums2[ind2]:
                nums[ind] = nums1[ind1]
                ind1 += 1
            else:
                nums[ind] = nums2[ind2]
                ind2 += 1
            ind += 1
        
        while ind1 < len(nums1):
            nums[ind] = nums1[ind1]
            ind1 += 1
            ind += 1
            
        while ind2 < len(nums2):
            nums[ind] = nums2[ind2]
            ind2 += 1
            ind += 1
        
    def mergeSort(self, nums: t.List[int], left: int, right: int) -> None:
        if left < right:
            mid: int = int((right - left) / 2) + left
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)

