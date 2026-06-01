import typing as t

class Solution:
    def successfulPairs(self, spells: t.List[int], potions: t.List[int], success: int) -> t.List[int]:
        result: t.List[int] = [0] * len(spells)
        self.mergeSort(potions, 0, len(potions) - 1)

        for ind in range(0, len(spells), 1):
            left: int = 0
            right: int = len(potions) - 1
            while left <= right:
                mid: int = int((right - left) / 2) + left
                pre_success: int = spells[ind] * potions[mid - 1] if mid - 1 >= 0 else 0
                cur_success: int = spells[ind] * potions[mid]
                if cur_success >= success:
                    if pre_success < success:
                        result[ind] = len(potions) - mid
                        break
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
        
        return result
    
    def merge(self, nums: t.List[int], left: int, mid: int, right: int) -> None:
        nums1: t.List[int] = nums[left : mid + 1]
        nums2: t.List[int] = nums[mid + 1 : right + 1]
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