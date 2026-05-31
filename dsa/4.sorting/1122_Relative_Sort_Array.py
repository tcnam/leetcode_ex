import typing as t

class Solution:
    def relativeSortArray(self, arr1: t.List[int], arr2: t.List[int]) -> t.List[int]:
        return self.method1(arr1, arr2)
    
    def method1(self, arr1: t.List[int], arr2: t.List[int]) -> t.List[int]:
        appear_set: t.Set[int] = set(arr2)
        freq_dict: t.Dict[int, int] = {}
        not_appear_list: t.List[int] = []
        result: t.List[int] = []

        for ind in range(0, len(arr1), 1):
            if arr1[ind] in appear_set:
                freq_dict[arr1[ind]] = (
                    freq_dict.get(arr1[ind]) + 1 
                    if arr1[ind] in freq_dict.keys() 
                    else 1
                )
            else:
                not_appear_list.append(arr1[ind])
        
        for ind in range(0, len(arr2), 1):
            result.extend([arr2[ind]] * freq_dict[arr2[ind]])
        
        self.mergeSort(not_appear_list, 0, len(not_appear_list) - 1)
        result.extend(not_appear_list)

        return result
    
    def merge(self, nums: t.List[int], left: int, mid: int, right: int) -> None:
        nums1: t.List[int] = nums[left : mid + 1]
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
            mid: int = int((right - left)/2) + left
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)