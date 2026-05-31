import typing as t

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # return self.method1(heights)
        return self.method2(heights)
    
    def method1(self, heights: t.List[int]) -> int:
        cp_heights: t.List[int] = [
            heights[ind] for ind in range(0, len(heights), 1)
        ]
        result: int = 0
        self.mergeSort(cp_heights, 0, len(cp_heights) - 1)

        for ind in range(0, len(heights), 1):
            if heights[ind] != cp_heights[ind]:
                result += 1
        
        return result
    
    def method2(self, heights: t.List[int]) -> int:
        freq_tracker_list: t.List[int] = [0] * 101
        result: int = 0

        for ind in range(0, len(heights), 1):
            freq_tracker_list[heights[ind]] += 1
        
        acc_sum_freq_tracker_list: t.List[int] = []
        acc_sum_freq: int = 0

        for ind in range(0, len(freq_tracker_list), 1):
            acc_sum_freq += freq_tracker_list[ind]
            acc_sum_freq_tracker_list.append(acc_sum_freq)
        
        for ind in range(0, len(heights), 1):
            curr_height: int = heights[ind]
            left_ind: int = acc_sum_freq_tracker_list[curr_height - 1]
            right_ind: int = acc_sum_freq_tracker_list[curr_height]
            if ind < left_ind or ind >= right_ind:
                result += 1

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