import typing as t

class Solution:
    def merge(self, nums1: t.List[int], m: int, nums2: t.List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ind1: int = m - 1
        ind2: int = n - 1
        ind: int = m + n - 1

        while ind1 >= 0 and ind2 >= 0:
            if nums1[ind1] > nums2[ind2]:
                nums1[ind] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[ind] = nums2[ind2]
                ind2 -= 1
            ind -= 1
        
        while ind2 >= 0:
            nums1[ind] = nums2[ind2]
            ind2 -= 1
            ind -= 1
        