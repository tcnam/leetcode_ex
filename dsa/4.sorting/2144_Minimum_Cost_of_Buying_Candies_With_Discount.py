import typing as t

class Solution:
    def minimumCost(self, cost: t.List[int]) -> int:
        # return self.method1(cost)
        return self.method2(cost)
    
    def method2(self, cost: t.List[int]) -> int:
        freq_tracker: t.List[int] = [0] * 101
        result: int = 0
        count: int = 0

        for ind in range (0, len(cost), 1):
            freq_tracker[cost[ind]] += 1
        
        for ind in range(len(freq_tracker) - 1, -1, -1):
            while freq_tracker[ind] > 0:
                if count < 2:
                    result += ind
                    freq_tracker[ind] -= 1
                    count += 1
                else:
                    freq_tracker[ind] -= 1
                    count = 0
        return result
            
    
    def method1(self, cost: t.List[int]) -> int:
        result: int = 0
        self.mergeSort(cost, 0, len(cost) - 1)
        for ind in range(0, len(cost), 1):
            if (ind + 1) % 3 != 0:
                result += cost[ind]
        return result
    
    def merge(self, nums: t.List[int], left: int, mid: int, right: int) -> None:
        nums1: t.List[int] = nums[left : mid + 1]
        nums2: t.List[int] = nums[mid + 1 : right + 1]
        ind1: int = 0
        ind2: int = 0
        ind: int = left

        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] > nums2[ind2]:
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
    
