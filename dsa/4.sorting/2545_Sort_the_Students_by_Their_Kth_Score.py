import typing as t

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        org_ind_dict: t.Dict[int, int] = {}
        k_score_list: t.List[int] = []
        result: t.List[List[int]] = []

        for ind in range(0, len(score), 1):
            curr_score: int = score[ind][k]
            org_ind_dict[curr_score] = ind
            k_score_list.append(curr_score)
        
        self.mergeSort(k_score_list, 0, len(k_score_list) - 1)

        for ind in range(0, len(k_score_list), 1):
            score_ind: int = org_ind_dict[k_score_list[ind]]
            result.append(score[score_ind])

        return result
    
    def merge(self, nums: t.List[int], left: int, mid: int, right: int) -> None:
        nums1: t.List[int] = nums[left : mid + 1]
        nums2: t.List[int] = nums[mid + 1: right + 1]
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
