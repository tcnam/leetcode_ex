import typing as t

class Solution:
    def targetIndices(self, nums: t.List[int], target: int) -> t.List[int]:
        result: t.List[int] = []
        self.mergeSort(nums, 0, len(nums) - 1)
        for ind in range(0, len(nums), 1):
            if nums[ind] == target:
                result.append(ind)
        return result
    
    def merge(self, nums: t.List[int], left: int, mid: int, right: int) -> None:
        nums1: t.List[int] = nums[left : mid + 1]
        nums2: t.List[int] = nums[mid + 1: right + 1]

        ind1: int = 0
        ind2: int = 0
        ind: int = left

        len_nums1: int = len(nums1)
        len_nums2: int = len(nums2)

        while ind1 < len_nums1 and ind2 < len_nums2:
            if nums1[ind1] < nums2[ind2]:
                nums[ind] = nums1[ind1]
                ind1 += 1
            else:
                nums[ind] = nums2[ind2]
                ind2 += 1
        
            ind += 1
        
        while ind1 < len_nums1:
            nums[ind] = nums1[ind1]
            ind1 += 1
            ind += 1
        
        while ind2 < len_nums2:
            nums[ind] = nums2[ind2]
            ind2 += 1
            ind += 1
    
    def mergeSort(self, nums: t.List[int], left: int, right: int) -> None:
        if left < right:
            mid: int = int((right - left)/2) + left
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)

    