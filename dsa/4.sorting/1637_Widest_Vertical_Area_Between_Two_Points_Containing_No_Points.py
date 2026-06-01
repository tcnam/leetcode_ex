import typing as t

class Solution:
    def maxWidthOfVerticalArea(self, points: t.List[t.List[int]]) -> int:
        return self.method1(points)

    def method1(self, points: t.List[t.List[int]]) -> int:
        points_x: t.List[int] = [
            points[ind][0] for ind in range(0, len(points), 1) 
        ]
        result: int = 0
        self.mergeSort(points_x, 0, len(points_x) - 1)
        for ind in range(1, len(points_x), 1):
            cur_vertical_area: int = points_x[ind] - points_x[ind - 1]
            if cur_vertical_area > result:
                result = cur_vertical_area
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
            mid: int = int((right - left) / 2) + left
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)