import typing as t

class Solution:
    def singleNonDuplicate(self, nums: t.List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = int((right - left) / 2) + left
            left_val: int = nums[mid - 1] if mid - 1 >= 0 else -1
            right_val: int = nums[mid + 1] if mid + 1 < len(nums) else -1

            if nums[mid] != left_val and nums[mid] != right_val:
                return nums[mid]

            if(
                (mid % 2 == 0 and nums[mid] == left_val)
                or
                (mid % 2 == 1 and nums[mid] == right_val)
            ):
                right = mid - 1
            else:
                left = mid + 1
        
        return -1 