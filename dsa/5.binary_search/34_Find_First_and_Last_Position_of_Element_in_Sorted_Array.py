import typing as t

class Solution:
    def searchRange(self, nums: t.List[int], target: int) -> t.List[int]:
        left: int = 0
        right: int = len(nums) - 1

        left_bound_ind: int = -1
        right_bound_ind: int = -1

        while left <= right:
            mid: int = int((right - left) / 2) + left
            prev_val: int = nums[mid - 1] if mid - 1 >= 0 else -pow(10, 9) - 1

            if nums[mid] == target:
                if prev_val < target:
                    left_bound_ind = mid
                    break
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid: int = int((right - left) / 2) + left
            next_val: int = nums[mid + 1] if mid + 1 < len(nums) else pow(10, 9) + 1
            if nums[mid] == target:
                if next_val > target:
                    right_bound_ind = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1



        return [left_bound_ind, right_bound_ind]