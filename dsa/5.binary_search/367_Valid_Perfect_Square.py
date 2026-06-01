class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left: int = 1
        right: int = num

        while left <= right:
            mid: int = int((right - left) / 2) + left
            pow2_val: int = mid * mid
            if pow2_val == num:
                return True
            elif pow2_val < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
